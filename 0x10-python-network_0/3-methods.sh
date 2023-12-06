#!/bin/bash
# A bash script that takes in a url and diplaus all http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
