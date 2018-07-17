# -*- coding: utf-8 -*-
"""
Created on Jul 16, 2018

@author: Wyliena Guan
@due date: 2016-07-20

@general instructions:
"""
import sys
import csv
import os

# Data structure
#    {'prescriber_last_name': [...], 
#    'drug_cost': [...], 
#    'id': [...], 
#    'prescriber_first_name': [...], 
#    'drug_name': [...],}

#    METHODS

def is_prescription(line_num, line):
    """
    Return true/false object from a string in prescription record format.
    Return true if the line is for a prescription.  False, otherwise. 
    """
    #id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
    #1000000001,Smith,James,AMBIEN,100
    #1000000002,Garcia,Maria,AMBIEN,200
    #1000000003,Johnson,James,CHLORPROMAZINE,1000
    #1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
    #1000000005,Smith,David,BENZTROPINE MESYLATE,1500
    currentline = line.split(",")
    
    pid = currentline[0]
    prescriber_last_name = currentline[1]
    prescriber_first_name = currentline[2]
    drug_name = currentline[3]
    drug_cost = currentline[4].rstrip()

#    print("pid==" + str(pid))
#    print("prescriber_last_name==" + str(prescriber_last_name))
#    print("prescriber_first_name==" + prescriber_first_name)
#    print("drug_name==" + str(drug_name))
#    print("drug_cost==" + str(drug_cost))
    
    try:
        if (len(currentline) == 5 and
            isinstance(int(pid), (int)) and
            len(prescriber_last_name) > 0 and
            not isinstance(prescriber_last_name, (int, float, complex)) and
            len(prescriber_first_name) > 0 and
            not isinstance(prescriber_first_name, (int, float, complex)) and
            len(drug_name) > 0 and
            isinstance(int(drug_cost), (int))
            ):
            return True
        else:
            print("line_num %10 is broken prescription data line", (line_num))
            return False
    except ValueError:
        return False
    
def is_non_zero_file(fpath):
    return (os.path.isfile(fpath) and os.path.getsize(fpath) > 0)

#############################################################################
#############################################################################

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    if len(sys.argv) < 3:
        sys.exit("Need output file argument")
    if len(sys.argv) > 3:
        print("Only input file argument and output file argument accepted")
except ValueError:
    sys.exit("Arguments should be input file and then output file")

cwd = os.getcwd()
fname = os.path.join(cwd, input_file.replace("./", ""))
outfile = os.path.join(cwd, output_file.replace("./", ""))

try:
    if not is_non_zero_file(fname):
        sys.exit("Empty input file")
except ValueError:
    sys.exit("Check input file errors")

# First, you should write Python code to process all the files for a given year
fid = open(fname, 'r', encoding='utf-8')

prescriptions = {}
headers = []
for line_num, line in enumerate(fid):
        # If line is for a prescription, create a list of info for 
        # prescriptions and append to master list "prescriptions"
        if line_num == 0:
            currentline = line.split(",")
            if len(currentline) != 5:
                sys.exit("wrong number of columns in file")
            for i in range(len(currentline)):
                headers.append(currentline[i].rstrip())
#        print(headers)
            for h in headers:
                prescriptions[h] = []
            
        if line_num > 0 and (is_prescription(line_num, line) == True):
            currentline = line.split(",")
            for h, v in zip(headers, currentline):
                prescriptions[h].append(v.rstrip())
print(prescriptions)

# produce the following output
#drug_name,num_prescriber,total_cost
#CHLORPROMAZINE,2,3000
#BENZTROPINE MESYLATE,1,1500
#AMBIEN,2,300

# get sorted list of drugs
myset = set(prescriptions['drug_name'])
mynewlist = sorted(list(myset))

newheaders = ['drug_name', 'num_prescriber', 'total_cost']
output = []

for drug in mynewlist:
    drug_ind = [i for i, j in enumerate(prescriptions['drug_name']) if j == 'AMBIEN']
    num_prescriber = len(drug_ind)
    total_cost = sum([int(prescriptions['drug_cost'][x]) for x in drug_ind])
    output.append([drug, num_prescriber, total_cost])

with open('top_cost_drug.txt', 'w') as outfile:
    mywriter = csv.writer(outfile)
    # manually add header

    mywriter.writerow(newheaders)
    for d in output:
        mywriter.writerow(d)