#!/bin/bash

dir_actual=$(pwd)
download_dir="files/download_files"

cd $download_dir

# Run the Python program using python3 with relative path
python3 $dir_actual/src/download.py -v -H 127.0.0.1 -p 3006 -n $1 -r

cd dir_actual