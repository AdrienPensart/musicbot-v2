#!/bin/sh

set -e
trap '[ $? -eq 0 ] && exit 0 || echo "$0 FAILED"' EXIT

bash gen-deps.sh
bash linting.sh
bash gen-doc.sh

kernel=`uname -r`
case "$kernel" in
*microsoft*) echo "No unit testing because docker not available" ;;
*       )
    echo "Running unit tests"
    poetry run pytest
    poetry run coverage-badge -f -o doc/coverage.svg
    git add doc/coverage.svg
    ;;
esac

exit 0
