#!/bin/bash

conda create -n rtfd_env python=3.9
conda activate rtfd_env

conda install pytorch torchvision cudatoolkit=11.3 -c pytorch
conda install -c 1adrianb face_alignment

python main.py ./input/v1.MP4
## or
#python main.py
