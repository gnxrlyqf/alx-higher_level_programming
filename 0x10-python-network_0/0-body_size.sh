#!/usr/bin/bash
#get the size of a curl response
curl -s -w "%{size_download}\n" "$1"
