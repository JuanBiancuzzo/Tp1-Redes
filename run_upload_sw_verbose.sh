#!/bin/bash

dir_actual=$(pwd)
upload_dir="files/upload_files"

cd $upload_dir

# Run the Python program using python3 with relative path
python3 $dir_actual/src/upload.py -q -H 127.0.0.1 -p 3006 -n $1 -w

cd $dir_actual