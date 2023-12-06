#!/bin/bash
# A bash script that displauys the size of the body of the url
response_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')
