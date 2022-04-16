#! /usr/bin/env bash

set -euo pipefail
cleanup() {
    git remote remove tmp_upstream > /dev/null
    git checkout $cur_branch > /dev/null
}

cur_branch=$(git branch --show-current)
old_advice=$(git config --get advice.detachedHead) && true

# Will compare to master.
git remote add tmp_upstream https://github.com/typeddjango/django-stubs || (cleanup && exit 2)
git fetch tmp_upstream --quiet

# Fetch last cache.
mkdir -p .custom_cache/
cur_hash=$(git rev-parse HEAD)  # Actual commit we're testing
git fetch tmp_upstream refs/notes/*:refs/notes/*  --quiet # Use * so that it won't fail on first run
git checkout tmp_upstream/master --quiet || (cleanup && exit 2)

ref_hash=$(git rev-parse HEAD)  # Try to compare with master
if [ "$ref_hash" = "$cur_hash" ]; then  # Already on master; compare to previous commit
    ref_hash=$(git rev-parse HEAD~1)
fi
git checkout $cur_branch

# Expected failure on first run
git notes --ref cache_history show $ref_hash > .custom_cache/.apply_errors && true
if [ $? -eq 0 ]; then
    # Doesn't matter how good it is: assign this result to commit
    ./scripts/compare_errors.py && true
    result=$?
    ./scripts/write_errors_cache.py
    # Always add even if it was set manually before
    git notes --ref cache_history add -f -F .custom_cache/.apply_errors
    git push origin refs/notes/cache_history
else
    echo 'No data for main branch yet - nothing to do.'
fi

cleanup
exit $result
