import re
import csv
from pprint import pprint

prereq_dict = {}
course_dict = {}

with open('cs_prereqs2018_2.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")
    for row in reader:
        course_id = row['SUBJECT'] + row['NUMB']
        prereqs = re.findall("(?:[A-Za-z/]*\s*[0-9X]{4}(?:\sor\s)*)+", row['PRE-REQ COURSES'])
        #print(prereqs, end="")
        #print(" : "  + row['NUMB'])                
        prereqs = [crse.split('or') for crse in [crse_clump.replace(" ","") for crse_clump in prereqs]]
        prereq_dict[course_id] = prereqs
        course_dict[course_id] = row['CRSE TITLE']

try:
    course = input("What course are you trying to take? : ").upper().replace(" ", "")
    print("Requirements for " + course_dict[course] + ": ")
    print(prereq_dict[course])
except:
    print("Incorrect course/course does not exist")

#pprint(prereq_dict)
#pprint(prereq_dict)

#NOTE: if crse in crse_clump has no subject (i.e. 4249), gets subject of first item in clump