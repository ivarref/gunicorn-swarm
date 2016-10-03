#!/bin/bash

set -ex

v=$(cat /dev/urandom | tr -dc 'a-z' | fold -w 4 | head -n 1)

docker build --tag=web:${v} .

docker service update --image web:${v} my_web