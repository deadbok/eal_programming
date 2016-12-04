#!/bin/sh

for I in 6 7 8 9 10; 
do
	echo prog$I.py
	pygmentize -o prog$I.rtf prog$I.py
done
