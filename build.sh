#!/bin/bash
cp ./deploy/$1/Dockerfile .
docker build -t $1 .
rm ./Dockerfile