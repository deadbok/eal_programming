#!/usr/bin/env bash

PY_FILES=(*.py)

for PY_FILE in "${PY_FILES[@]}"
do
	echo ${PY_FILE}
	pygmentize -o "`basename "${PY_FILE}" .py`.rtf" "${PY_FILE}"
	python3 py2puml.py ${PY_FILE}
	java -jar plantuml.jar ${PY_FILE}.puml
done
