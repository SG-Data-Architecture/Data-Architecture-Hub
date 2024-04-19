#!/bin/bash

: << 'comment'
The set up herein is in line with the Dockerfile set up.  Both use the same
requirements.txt file to create an environment.
comment

# The environment in focus
prefix=/opt/miniconda3/envs/transcribe

# Delete the existing <transcribe> environment
conda remove -y --prefix $prefix --all

# Rebuild environment <transcribe> via a requirements.txt file
conda env create -f environment.yml -p $prefix
