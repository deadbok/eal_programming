#!/usr/bin/env bash

PY_FILES=(*.py)

for PY_FILE in "${PY_FILES[@]}"
do
	echo ${PY_FILE}
	pygmentize -o "`basename "$file" .py`.rtf" "${PY_FILE}"
done
