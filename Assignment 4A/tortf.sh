#!/usr/bin/env bash

for I in 1 2 3 4 5 6;
do
	echo prog$I.py
	pygmentize -o prog$I.rtf prog$I.py
done
