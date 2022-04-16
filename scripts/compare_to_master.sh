#! /usr/bin/env bash

set -euo pipefail
cleanup() {
    git remote remove tmp_upstream > /dev/null
    git checkout $cur_branch > /dev/null
    exit 1
}

cur_branch=$(git branch --show-current)
old_advice=$(git config --get advice.detachedHead) && true

# Will compare to master.
git remote add tmp_upstream https://github.com/typeddjango/django-stubs || cleanup
git fetch tmp_upstream --quiet

# Fetch last cache.
mkdir -p .custom_cache/
cur_hash=$(git rev-parse HEAD)  # Actual commit we're testing
git fetch tmp_upstream refs/notes/*:refs/notes/*  --quiet # Use * so that it won't fail on first run
git checkout tmp_upstream/master --quiet || cleanup

ref_hash=$(git rev-parse HEAD)  # Try to compare with master
if [ "$ref_hash" = "$cur_hash" ]; then  # Already on master; use previous commit
    ref_hash=$(git rev-parse HEAD^1)
fi
git checkout $cur_branch

# Expected failure on first run
git notes --ref cache_history show $ref_hash > .custom_cache/.apply_errors && true
if [ $? -eq 0 ]; then
    ./scripts/compare_errors.py || cleanup
    ./scripts/write_errors_cache.py
    git notes --ref cache_history add -F .custom_cache/.apply_errors
    git push origin refs/notes/cache_history
else
    echo 'No data for main branch yet - nothing to do.'
fi
cleanup || exit 0
