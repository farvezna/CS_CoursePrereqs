import re
import csv
from pprint import pprint

prereq_dict = {}
course_dict = {}

with open('cs_prereqs2018_2.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")
    for row in reader:
        course_id = row['SUBJECT'] + row['NUMB']
        prereq_dict[course_id] = row['PRE-REQ COURSES']
        course_dict[course_id] = row['CRSE TITLE']

course = input("What course are you trying to take? : ").upper().replace(" ", "")
#course = "".join([char if char != " " else "" for char in course])
print("Requirements for " + course_dict[course] + ": ")
print(prereq_dict[course])

#TODO: regex of prereq courses, List for OR's, tuple in list for AND's