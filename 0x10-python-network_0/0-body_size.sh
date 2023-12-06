#!/usr/bin/env bash
# A bash script that displauys the size of the body of the url

# Check if a url is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <url>"
	exit 1
fi

response_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

if [ -z "$response_size" ]; then
	echo "Unable to retrieve the response size"
else
	echo "Response size: ${response_size} bytes"
fi
