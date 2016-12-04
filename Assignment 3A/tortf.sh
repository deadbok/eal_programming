#!/usr/bin/env bash

for I in 1 2 3 5;
do
	echo prog$I.py
	pygmentize -o prog$I.rtf prog$I.py
done
