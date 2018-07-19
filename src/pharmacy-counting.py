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
def check_input_ids(fname):
    """
    Return true if there are no duplicates of id in input file
    Return false otherwise
    """
    fid = open(fname, 'r', encoding='utf-8')    
    
    list_id = []
    for line_num, line in enumerate(fid):
        if line_num == 0:
            currentline = line.split(",")
            if currentline[0] != "id":
                raise Exception("first column is not 'id'")
        if line_num > 0:
            currentline = line.split(",")
            list_id.append(currentline[0])
    return len(list_id) == len(set(list_id))
        

def is_prescription(line_num, line):
    """
    Return true/false object from a string in prescription record format.
    Return true if the line is for a prescription.  False, otherwise. 
    """
#    id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
#    1000000001,Smith,James,AMBIEN,100
#    1000000002,Garcia,Maria,AMBIEN,200
#    1000000003,Johnson,James,CHLORPROMAZINE,1000
#    1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
#    1000000005,Smith,David,BENZTROPINE MESYLATE,1500
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
    """
    Returns true if file is non-empty
    Returns false if file is empty
    """
    return (os.path.isfile(fpath) and os.path.getsize(fpath) > 0)

def duplicates(lst, item):
    """
    Returns indices of designated in list
    """
    return [i for i, x in enumerate(lst) if x == item]

#############################################################################
#############################################################################
# check that python 3 is being run
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

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

#print(fname)
#print(outfile)

try:
    if not is_non_zero_file(fname):
        sys.exit("Empty input file")
except ValueError:
    sys.exit("Check input file errors")

# test files
#fname = '/Users/sag129/Desktop/pharmacy_counting/insight_testsuite/tests/test_1/input/itcont.txt'
#outfile = '/Users/sag129/Desktop/pharmacy_counting/insight_testsuite/tests/test_1/output/top_cost_drug.txt'

#fname = '/Users/sag129/Desktop/pharmacy_counting/insight_testsuite/tests/your-own-test_1/input/itcont.txt'
#outfile = '/Users/sag129/Desktop/pharmacy_counting/insight_testsuite/tests/your-own-test_1/output/top_cost_drug.txt'

# check if there are any duplicates in ids
if check_input_ids(fname) == False:
    raise Exception("Duplicates of id present in input file")

# First, you should write Python code to process all the files for a given year
fid = open(fname, 'r', encoding='utf-8')

prescriptions = {}
headers = []

 # If line is for a prescription, create a list of info for 
# prescriptions and append to master list "prescriptions"
for line_num, line in enumerate(fid):
    if line_num == 0:
        currentline = line.split(",")
        if len(currentline) != 5:
            sys.exit("wrong number of header columns in file")
        for i in range(len(currentline)):
            headers.append(currentline[i].rstrip())
        for h in headers:
            prescriptions[h] = []
        
    if line_num > 0 and (is_prescription(line_num, line) == True):
        currentline = line.split(",")
        if len(currentline) != 5:
            sys.exit("wrong number of columns in file for row %10", line_num)
    output['num_prescriber'].append(num_prescriber)
    output['total_cost'].append(total_cost)

# order total cost in descending order based on total drug cost
sort_tc = sorted(output['total_cost'], reverse=False)

myList = output['total_cost']
sort_tc_ind = [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
rev_tc_ind = sort_tc_ind[::-1]

# re-order lists in output dictionary
#target = [output['total_cost'][x] for x in rev_tc_ind]
output['total_cost'] = [output['total_cost'][x] for x in rev_tc_ind]

column_not_tc = [i for i in newheaders if i!='total_cost']

for h in column_not_tc:
    output[h] = [output[h][x] for x in rev_tc_ind]

#print(output)

# break tie by ordering by ascending drug name
myset1 = set(output['total_cost'])
mynewlist1 = list(myset1)

for tot_cost in mynewlist1:
    dup_ind = duplicates(output['total_cost'], 3000)
    # ^ index of duplicate total_cost values for specific total_cost value
    
    if len(dup_ind) > 1:
        tie_drug_names = [output['drug_name'][x] for x in dup_ind]
        # ^ find corresponding drug_names of duplicate total_cost values
        
        # create a dictionary {drug_name1: original_index}
        d = {}
        for k, v in zip(tie_drug_names, dup_ind):
            d[k] = v
        
        # sort tied drug_names alphabetically
        sort_drug_names = sorted(tie_drug_names)
        # get corresponding new indices for each sorted drug name
        sort_drug_ind = [d[i] for i in sort_drug_names]
        
        # re-sort output table for duplicates of total_value by sort_drug_ind
    #    output['drug_name'][pos] = [output['drug_name'][x] for x in sort_drug_ind][target]
        
        for h in newheaders:
            target = [output[h][x] for x in sort_drug_ind]
            pos = dup_ind
            for x,y in zip(pos,target):
                output[h][x] = y
    else:
        continue        

#print(output)

with open(outfile, 'w+') as out:
    mywriter = csv.writer(out)
    # manually add header
    mywriter.writerow(newheaders)
    
    nrow = len(output['total_cost'])
    for i in range(nrow):
        row = [output['drug_name'][i], output['num_prescriber'][i], output['total_cost'][i]]
        mywriter.writerow(row)

print("Writing outfile complete")