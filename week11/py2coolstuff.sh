#!/usr/bin/env bash

PY_FILES=(*.py)

for PY_FILE in "${PY_FILES[@]}"
do
	echo ${PY_FILE}
#	pygmentize -o "`basename "${PY_FILE}" .py`.rtf" "${PY_FILE}"
#	python3 py2puml.py ${PY_FILE}
done

PUML_FILES=(*.puml)

for PUML_FILE in "${PUML_FILES[@]}"
do
	echo ${PUML_FILE}
	java -jar plantuml.jar ${PUML_FILE}
done