# InsightDataScience/pharmacy_counting Data Challenge

Imagine you are a data engineer working for an online pharmacy. This program generates a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3 needs to be installed (https://www.python.org/getit/).
Internal packages (sys, csv, os) are used in pharmacy-counting.py program.

### Installing

Github repository can be cloned from https://github.com/sag129/pharmacy_counting

## Running the tests

Run the following commands
sh ./run_tests.sh in sag129/pharmacy_counting/insight_testsuite/ directory

### Break down into end to end tests

Check for basic functionality of program
Test_1 - tests to see if total_costs are calculated and sorted in descending order
Test_2 - tests to see if total_costs are calculated and sorted in descending order and
                      if tied total_costs are sorted in ascending order by drug name

Test for program being able to catch problems
Test_3 - tests to see if duplicate id numbers are present.  Should see error message below:
```
Duplicates of id present in input file
```

Test_4 - tests to see if input file is empty.  Should see error message below:
```
Empty input file
```

Test_5 - tests to see if input file has empty values for any column - if so, should skip these lines and raise error message.  Output file will still be generated.  Should see error message and output file below:
```
broken prescription data line at line 2
broken prescription data line at line 4
broken prescription data line at line 5
Writing outfile complete
```
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,1,1000
AMBIEN,1,100
```

Test_6 - tests to see if input file has wrong type of values for any column - if so, should skip these lines and show an error message.  Output file will still be generated.  Should see error message and output file below:
```
broken prescription data line at line 4
Writing outfile complete
```

```
drug_name,num_prescriber,total_cost
BENZTROPINE MESYLATE,1,1500
CHLORPROMAZINE,1,1000
AMBIEN,2,300
```

## Deployment

Run pharmacy counting program (./src/pharmacy-counting.py) on your input file of choice (./input/itcont.txt)
This will produce output file (./output/top_cost_drug.txt).

sh ./run.sh

## Built With

* [Python 3](https://www.python.org/getit/) - Version of Python used

## Authors

* **Wyliena Guan** - [sag129](https://github.com/sag129)

