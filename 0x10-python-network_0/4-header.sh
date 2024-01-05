#!/bin/bash
#get the response of code 200
curl -sX GET -H "X-School-User-Id: 98" "$1" -L
