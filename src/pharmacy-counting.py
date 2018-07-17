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

# check that python 3 is being run
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


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

def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

#############################################################################
#############################################################################

#input_file = sys.argv[1]
#output_file = sys.argv[2]
#
#try:
#    if len(sys.argv) < 3:
#        sys.exit("Need output file argument")
#    if len(sys.argv) > 3:
#        print("Only input file argument and output file argument accepted")
#except ValueError:
#    sys.exit("Arguments should be input file and then output file")
#
#cwd = os.getcwd()
#fname = os.path.join(cwd, input_file.replace("./", ""))
#outfile = os.path.join(cwd, output_file.replace("./", ""))
#
##print(fname)
##print(outfile)
#
#try:
#    if not is_non_zero_file(fname):
#        sys.exit("Empty input file")
#except ValueError:
#    sys.exit("Check input file errors")

fname = '/Users/sag129/Desktop/pharmacy_counting/insight_testsuite/tests/test_1/input/itcont.txt'
outfile = '/Users/sag129/Desktop/pharmacy_counting/insight_testsuite/tests/test_1/output/top_cost_drug.txt'

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
mynewlist = list(myset)

newheaders = ['drug_name', 'num_prescriber', 'total_cost']
output = {}

for h in newheaders:
    output[h] = []

# create [[drug, num_prescriber, total_cost], [...], [...]]
for drug in mynewlist:
    drug_ind = [i for i, j in enumerate(prescriptions['drug_name']) if j == drug]
    num_prescriber = len(drug_ind)
    total_cost = sum([int(prescriptions['drug_cost'][x]) for x in drug_ind])
    output['drug_name'].append(drug)
    output['num_prescriber'].append(num_prescriber)
    output['total_cost'].append(total_cost)

# order in descending order based on total drug cost
# print(sorted(output['total_cost'], reverse=True))
rev_tc = list(reversed(output['total_cost']))
rev_tc_ind = sorted(range(len(output['total_cost'])), key=lambda k: rev_tc[k])

# re-order lists in output dictionary
for h in newheaders:
    output[h] = [output[h][x] for x in rev_tc_ind]

# break tie by ordering by ascending drug name
myset1 = set(output['total_cost'])
mynewlist1 = list(myset1)

for total_cost in mynewlist1:
#   index of duplicate total_cost values for specific total_cost value
    dup_ind = duplicates(output['total_cost'], 3000)
#   find corresponding drug_names of duplicate total_cost values
    tie_drug_names = [output['drug_name'][x] for x in dup_ind]
    
    d = {}
    for k, v in zip(tie_drug_names, dup_ind):
        d[k] = v
    # sort tied drug_names alphabetically
    sort_drug_names = sorted(tie_drug_names)
    sort_drug_ind = [d[i] for i in sort_drug_names]
    
    # order by ascending drug name - 
    [dup_ind, sort_drug_ind]
    # sort_drug_ind
    [output['num_prescriber'][x] for x in sort_drug_ind]
    [output['num_prescriber'][x] for x in sort_drug_ind]
    [output['total_cost'][x] for x in sort_drug_ind]

        

with open(outfile, 'w+') as out:
    mywriter = csv.writer(out)
    # manually add header

    mywriter.writerow(newheaders)
    for d in output:
        mywriter.writerow(d)