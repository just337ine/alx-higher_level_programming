#!/bin/bash
# A bash script that takes in a url and diplaus all http methods
if [ -z "$1" ]; then
	echo "Usage: $0 <url>"
	exit 1
fi
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
