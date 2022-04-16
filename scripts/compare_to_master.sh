#! /usr/bin/env bash

set -euxo pipefail
cleanup() {
    git remote remove tmp_upstream > /dev/null
    git checkout $cur_branch > /dev/null
    git branch -D upstream_master > /dev/null
}

cur_branch=$(git branch --show-current)

# Will compare to master.
git remote add tmp_upstream https://github.com/typeddjango/django-stubs || (cleanup && exit 2)
git fetch tmp_upstream

# Fetch last cache.
mkdir -p .custom_cache/
cur_hash=$(git rev-parse HEAD)  # Actual commit we're testing
git fetch tmp_upstream refs/notes/*:refs/notes/*  --quiet # Use * so that it won't fail on first run
git checkout -b upstream_master --track tmp_upstream/master || (cleanup && exit 2)

git rev-parse upstream_master^
# Try to compare with master
ref_hash=$(git rev-parse upstream_master)
if [ "$ref_hash" = "$cur_hash" ]; then
    # Already on master; compare to previous commit
    ref_hash=$(git rev-parse upstream_master^)
fi

# Get result of run on ref_hash (should fail on first workflow run)
git notes --ref cache_history show $ref_hash > .custom_cache/.apply_errors && true
if [ $? -eq 0 ]; then
    ./scripts/compare_errors.py && true
    result=$?
else
    echo 'No data for main branch yet - nothing to do.'
    result=0
fi

./scripts/write_errors_cache.py
# Set identity for note
git config --global user.email "django_stubs_test@example.com"
git config --global user.name "Cache writing bot"
# Always add even if it was set manually before
git -c 'user.email=django_stubs_test@example.com' -c 'user.name=Cache writing bot' notes --ref cache_history add -f -F .custom_cache/.apply_errors $cur_hash
git push origin refs/notes/cache_history

cleanup
exit $result
