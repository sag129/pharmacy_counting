#!/bin/bash
#
# This code assumes that the correct version of the output file is in the output folder.
# We test against these correct output files.

chmod +x ./run_tests.sh

# copy correct output file
cp ./tests/test_1/output/top_cost_drug.txt ./tests/test_1/output/top_cost_drug_correct.txt

# run python program
python ../src/pharmacy-counting.py ./tests/test_1/input/itcont.txt ./tests/test_1/output/top_cost_drug.txt

# check for differences between output and correct output
diff -q ./tests/test_1/output/top_cost_drug.txt ./tests/test_1/output/top_cost_drug_correct.txt 1>/dev/null
if [[ $? == "0" ]]
then
  # show a message for passing test
  echo "[PASS]: test_1"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="1 of 1 tests passed"
  echo $MSG

  # remove correct output file since it is the same as the output file
  rm ./tests/test_1/output/top_cost_drug_correct.txt
else
  # show a message for failing test
  echo "[FAIL]: test_1"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="0 of 1 tests passed"
  echo $MSG

  # remove bad output file
  rm ./tests/test_1/output/top_cost_drug.txt
  # rename correct output file with original output file name
  mv ./tests/test_1/output/top_cost_drug_correct.txt ./tests/test_1/output/top_cost_drug.txt
fi

# copy correct output file
cp ./tests/test_2/output/top_cost_drug.txt ./tests/test_2/output/top_cost_drug_correct.txt

# run python program
python ../src/pharmacy-counting.py ./tests/test_2/input/itcont.txt ./tests/test_2/output/top_cost_drug.txt

# check for differences between output and correct output
diff -q ./tests/test_2/output/top_cost_drug.txt ./tests/test_2/output/top_cost_drug_correct.txt 1>/dev/null
if [[ $? == "0" ]]
then
  # show a message for passing test
  echo "[PASS]: test_2"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="1 of 1 tests passed"
  echo $MSG

  # remove correct output file since it is the same as the output file
  rm ./tests/test_2/output/top_cost_drug_correct.txt
else
  # show a message for failing test
  echo "[FAIL]: test_2"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="0 of 1 tests passed"
  echo $MSG

  # remove bad output file
  rm ./tests/test_2/output/top_cost_drug.txt
  # rename correct output file with original output file name
  mv ./tests/test_2/output/top_cost_drug_correct.txt ./tests/test_2/output/top_cost_drug.txt
fi

####

# copy correct output file
cp ./tests/test_3/output/error.txt ./tests/test_3/output/error_correct.txt

# run python program
python ../src/pharmacy-counting.py ./tests/test_3/input/itcont.txt ./tests/test_3/output/top_cost_drug.txt &> ./tests/test_3/output/error.txt

# check for differences between output and correct output
diff -q ./tests/test_3/output/error.txt ./tests/test_3/output/error_correct.txt 1>/dev/null
if [[ $? == "0" ]]
then
  # show a message for passing test
  echo "[PASS]: test_3"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="1 of 1 tests passed"
  echo $MSG

  # remove correct output file since it is the same as the output file
  rm ./tests/test_3/output/error_correct.txt
else
  # show a message for failing test
  echo "[FAIL]: test_3"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="0 of 1 tests passed"
  echo $MSG

  # remove bad output file
  rm ./tests/test_3/output/error.txt
  # rename correct output file with original output file name
  mv ./tests/test_3/output/error_correct.txt ./tests/test_3/output/error.txt
fi

####

# copy correct output file
cp ./tests/test_4/output/error.txt ./tests/test_4/output/error_correct.txt

# run python program
python ../src/pharmacy-counting.py ./tests/test_4/input/itcont.txt ./tests/test_4/output/top_cost_drug.txt &> ./tests/test_4/output/error.txt

# check for differences between output and correct output
diff -q ./tests/test_4/output/error.txt ./tests/test_4/output/error_correct.txt 1>/dev/null
if [[ $? == "0" ]]
then
  # show a message for passing test
  echo "[PASS]: test_4"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="1 of 1 tests passed"
  echo $MSG

  # remove correct output file since it is the same as the output file
  rm ./tests/test_4/output/error_correct.txt
else
  # show a message for failing test
  echo "[FAIL]: test_4"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="0 of 1 tests passed"
  echo $MSG

  # remove bad output file
  rm ./tests/test_4/output/error.txt
  # rename correct output file with original output file name
  mv ./tests/test_4/output/error_correct.txt ./tests/test_4/output/error.txt
fi

####

# copy correct output file
cp ./tests/test_5/output/error.txt ./tests/test_5/output/error_correct.txt
cp ./tests/test_5/output/top_cost_drug.txt ./tests/test_5/output/top_cost_drug_correct.txt

# run python program
python ../src/pharmacy-counting.py ./tests/test_5/input/itcont.txt ./tests/test_5/output/top_cost_drug.txt &> ./tests/test_5/output/error.txt

# check for differences between output and correct output
diff -q ./tests/test_5/output/error.txt ./tests/test_5/output/error_correct.txt 1>/dev/null

if [[ $? == "0" ]]
then
  diff -q ./tests/test_5/output/top_cost_drug.txt ./tests/test_5/output/top_cost_drug_correct.txt 1>/dev/null
  if [[ $? == "0" ]]
  then
  # show a message for passing test
  echo "[PASS]: test_5"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="1 of 1 tests passed"
  echo $MSG

  # remove correct output file since it is the same as the output file
  rm ./tests/test_5/output/top_cost_drug_correct.txt
  # remove correct error file since it is the same as the error file
  rm ./tests/test_5/output/error_correct.txt

  else
  # show a message for failing test - wrong output file
    echo "[FAIL]: test_5"
    MSG="["
    NOW=$(date)
    MSG+=$NOW
    MSG+="] "
    MSG+="0 of 1 tests passed"
    echo $MSG

    # remove bad output file
    rm ./tests/test_5/output/top_cost_drug.txt
    # rename correct output file with original output file name
    mv ./tests/test_5/output/top_cost_drug_correct.txt ./tests/test_5/output/top_cost_drug.txt
  fi
else
  # show a message for failing test - wrong error message
  echo "[FAIL]: test_5"
  MSG="["
  NOW=$(date)
  MSG+=$NOW
  MSG+="] "
  MSG+="0 of 1 tests passed"
  echo $MSG

  # remove bad output file
  rm ./tests/test_5/output/error.txt
  # rename correct output file with original output file name
  mv ./tests/test_5/output/error_correct.txt ./tests/test_5/output/error.txt
fi
