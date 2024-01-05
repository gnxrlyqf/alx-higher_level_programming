#!/bin/bash
#get the size of a curl response
curl -s -o /dev/null -w "%{http_code}\n" "$1"
