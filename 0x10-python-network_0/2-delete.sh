#!/bin/bash
# A script that send delete request to a url
if [ -z "$1" ]; then
	echo "Usage: "$0" <url>"
	exit 1
fi
curl -sX DELETE "$1"
