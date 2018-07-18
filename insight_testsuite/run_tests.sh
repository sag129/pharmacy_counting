#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
chmod +x ./run_tests.sh

python ../src/pharmacy-counting.py ./tests/test_1/input/itcont.txt ./tests/test_1/output/top_cost_drug.txt

python ../src/pharmacy-counting.py ./tests/your-own-test_1/input/itcont.txt ./tests/your-own-test_1/output/top_cost_drug.txt

python ../src/pharmacy-counting.py ./tests/your-own-test_1/input/itcont1.txt ./tests/your-own-test_1/output/top_cost_drug1.txt