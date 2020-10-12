#!/bin/bash

#
# Tests the given ruleset (as first argument) on set of numbers.
#

if [ -z $1 ]; then
	echo "Rules not given.."
	exit 1
fi

for i in $( seq 2 30 ); do
	num=$(( i * i ))
	sqrt=$( ./cartist.py -s --rules "$1" $num)
	echo -en "\033[0m√$num = $sqrt "
	if [ $sqrt = $i ]; then
		echo -e "\e[32m[OK]"
	else
		echo -e "\e[31m[FAIL]"
	fi
done
