#!/bin/bash
__doc__="Checks that all notebooks can be executed sucessfully.

This assumes that you are running in an evironment where you have installed
all dependencies.
"
set -eu -o pipefail

RED="\e[31m"
RESET="\e[0m"
GREEN="\e[0;32m"
YELLOW="\e[0;33m"

function linebreak {
    echo ==============================================================
}

THISDIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")

COUNT_FAILED=0
FAILS=()
# shellcheck disable=SC2231 # We _WANT_ this to word-split
for NOTEBOOK in ${THISDIR}/../iris-mesh-tutorial/notebooks/*.ipynb; do
    linebreak
    NAME=$(basename "${NOTEBOOK}")
    if jupyter execute "${NOTEBOOK}"; then
        echo -e "✅ ${GREEN}TEST PASSED: execute ${NAME}${RESET}"
    else
        echo -e "❌ ${RED}TEST FAILED: execute ${NAME}${RESET}"
        ((COUNT_FAILED += 1))
        FAILS+=("${NAME}")
    fi
done

linebreak
echo -e "${YELLOW}WARNING - These test only check that workbooks"
echo -e "run and not that output is correct or content up-to-date${RESET}"

if [[ $COUNT_FAILED -gt 0 ]]; then
    echo -e "❌ ${RED}${COUNT_FAILED} Tests Failed:"
    for failure in "${FAILS[@]}"; do
        echo -e "* ${failure}"
    done
    exit 1
else
    echo -e "✅ ${GREEN}All tests passed${RESET}"
fi
