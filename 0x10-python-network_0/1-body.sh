#!/bin/bash
#get the response of code 200
if [ $(curl -s -o /dev/null -w "%{http_code}\n" "$1") -eq 200 ]; then curl -Ls "$1"; fi
