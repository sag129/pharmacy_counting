#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
chmod +x ./run_tests.sh

if command ; then
    echo "[FAIL]: test_1"
    echo "0 of 1 tests passed"
else
    echo "Command failed"
fi

cp ./tests/test_1/output/top_cost_drug.txt ./tests/test_1/output/top_cost_drug_correct.txt

python ../src/pharmacy-counting.py ./tests/test_1/input/itcont.txt ./tests/test_1/output/top_cost_drug.txt

diff -q ./tests/test_1/output/top_cost_drug.txt ./tests/test_1/output/top_cost_drug_correct.txt 1>/dev/null
if [[ $? == "0" ]]
then
  echo "[PASS]: test_1"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="1 of 1 tests passed"
  echo $MSG
else
  echo "[FAIL]: test_1"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="0 of 1 tests passed"
  echo $MSG
fi

rm ./tests/test_1/output/top_cost_drug_correct.txt

python ../src/pharmacy-counting.py ./tests/your-own-test_1/input/itcont.txt ./tests/your-own-test_1/output/top_cost_drug.txt



python ../src/pharmacy-counting.py ./tests/your-own-test_1/input/itcont1.txt ./tests/your-own-test_1/output/top_cost_drug1.txt