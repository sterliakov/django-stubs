#! /usr/bin/env bash

set -euxo pipefail
cleanup() {
    git checkout "$curr_branch"
    if [ "$should_stash" -eq 1 ]; then
        git stash pop
    fi
    git remote remove tmp_upstream_12753 > /dev/null
}

# Will compare to master.
# git remote add tmp_upstream_12753 https://github.com/typeddjango/django-stubs || (cleanup && exit 2)
git remote add tmp_upstream_12753 https://github.com/sterliakov/django-stubs || (cleanup && exit 2)
git fetch tmp_upstream_12753 --quiet

# Write cache for local version
mkdir -p .custom_cache/
./scripts/reapply_types.py -o local.json "$@"

# Check if there are local unstaged changes
curr_branch=$(git branch --show-current)
should_stash=$([ "$(git diff | wc -l)" ] && echo 1 || echo 0)
if [ "$should_stash" -eq 1 ]; then
    git stash
fi

# Switch to master
# git checkout tmp_upstream_12753/master
git checkout tmp_upstream_12753/ci_test >& /dev/null
./scripts/reapply_types.py -o master.json "$@"

./scripts/compare_errors.py local.json master.json

cleanup
