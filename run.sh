#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
# chmod a+rx ./run.sh
# check which python
# which python
# echo $PWD
chmod +x ./run.sh

python ./src/pharmacy-counting.py ./input/itcont.txt ./output/top_cost_drug.txt