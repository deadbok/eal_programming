#!/usr/bin/env bash

PY_FILES=(`find "$1" -name "*.py" -type f`)
SCRIPT_DIR=$(dirname "$0")

echo [Converting Python files]
for PY_FILE in "${PY_FILES[@]}"
do
    NAME=$(basename "${PY_FILE}")
    DIR=$(dirname "${PY_FILE}")
    DIR="${DIR#.}"
    DIR="${DIR#/}"
    OUTPUT_NAME="$2/${DIR////_}"
    if [[ "${OUTPUT_NAME}" == "*/" ]]
then
    OUTPUT_NAME="${OUTPUT_NAME}_"
fi
    OUTPUT_NAME="${OUTPUT_NAME}${NAME}"
	echo "${PY_FILE} -> ${OUTPUT_NAME}.{rtf puml}"
	pygmentize -o "${OUTPUT_NAME}.rtf" "${PY_FILE}"
	python3 ${SCRIPT_DIR}/py2puml.py ${PY_FILE} ${OUTPUT_NAME}.puml
done

PUML_FILES=($2/*.puml)

echo [Converting Plant UML files]
for PUML_FILE in "${PUML_FILES[@]}"
do
    NAME=$(basename "${PUML_FILE}")
	echo "${PUML_FILE} -> $2/${NAME}.png"
	java -jar ${SCRIPT_DIR}/plantuml.jar ${PUML_FILE}
done

HTML_FILES=(`find "$1" -name "*.html" -type f`)

echo [Converting HTML files]
for HTML_FILE in "${HTML_FILES[@]}"
do
    NAME=$(basename "${HTML_FILE}")
	echo "${HTML_FILE} -> ${2}/${NAME}.rtf"
	pygmentize -o "$2/${NAME}.rtf" "${HTML_FILE}"
done
