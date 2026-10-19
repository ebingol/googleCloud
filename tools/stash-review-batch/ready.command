#!/bin/sh
cd -- "$(dirname -- "$0")" || exit 1
python3 stash_batch.py ready "$@"
result=$?
printf "\nKapatmak icin Enter..."
read -r answer
exit "$result"
