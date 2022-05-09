#!/bin/bash

# docker \
#     run \ 
#     # https://docs.docker.com/storage/volumes/#choose-the--v-or---mount-flag
#     # pwd- present working directory - source:destination
#     --volume `pwd`/sample_data:/data \  
#     # https://docs.docker.com/engine/reference/run/#foreground
#     -it \ 
#     # https://docs.docker.com/engine/reference/run/#general-form
#     phrase_counter:v1 

docker \
    run \
    --volume `pwd`/sample_data:/data \
    -it \
    phrase_counter:v1 