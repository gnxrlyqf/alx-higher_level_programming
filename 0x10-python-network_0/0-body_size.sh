#!/usr/bin/bash
#get the size of a curl response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
