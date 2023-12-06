#!/bin/bash
# A bash script that takes in a url, sends a Get request ...

if [ -z "$1" ]; then
	echo "Usage: $0 <url>"
	exit 1
fi

curl -sL "$1"
