#!/bin/bash
# A bash script that displauys the size of the body of the url
curl -s "$1" | wc -c
