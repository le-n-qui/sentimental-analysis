# LIN 127 Project
# Student Evaluations and Course Grades
# Qui Le
# 03/16/2018

import sys
import csv
import nltk

from csv import DictReader
from collections import defaultdict

# first argument in the command line is average_grade.py
# secone argument in the command line: name of the csv file
filename = sys.argv[1]

# result is the name of the file 
# that will store information 
# at the end of execution
result = "average_grade.csv"

# Assign average for each letter grade 
# in this grade scale from UC Davis
# example: if a student gets a A+, we 
# translate that into 98.5, resulting from (97+100)/2
grade_scale = {'A+': 98.5, 'A': 95, 'A-': 91.5, 'B+': 88.5,
				'B': 85, 'B-': 81.5, 'C+': 78.5, 'C': 75, 'C-': 71.5,
				'D+': 68.5, 'D': 65, 'D-': 61.5, 'F': 55, 'N/A': 0}

# each value in each column is appended to a list
columns = defaultdict(list)

# counter variables
index = 0

# Open csv file
with open(filename, newline='') as f:
	# read rows into a dictionary format
	filereader = DictReader(f)
	
	# read a row 
	for row in filereader:
		# go over each column name and value
		for (k,v) in row.items():
			# append the value into appropriate list based on column name k
			columns[k].append(v)

		for key, _ in grade_scale.items():
			if row['Grade Received'] == key and row['Professor'] == columns['Professor'][index]:
				# open new files using professor names 
				# and write to each file student's grades
				# as reported on RateMyProfessor
				with open('/Users/lnq/Downloads/rmp_test_data/'+row['Professor'], 'a') as file:
					file.write(row['Grade Received'])
					file.write('\n')
		index += 1

# Open and create a csv file
# with three columns
with open(result, 'w') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(["Professor", "Student Average Grade", "Letter Grade"])

# remove duplicates and make a list of professor names
professorNames = list(set(columns['Professor']))
for name in professorNames:
	num_grades = 0
	total_points = 0
	
	# open each file of each professor 
	with open('/Users/lnq/Downloads/rmp_test_data/'+name) as f:
		for line in f:
			for key, value in grade_scale.items():
				if line.rstrip() == key and key != 'N/A':
					num_grades += 1
					total_points += value
	# Output name of professor and average grade 
	# calculated from grades received by former students 
	# If students who gave reviews provide no grades received in class, 
	# Average grade is N/A (Not Applicable)
	with open(result, 'a') as file1:
		writer = csv.writer(file1, delimiter=',')
		try:
			avg_grade = total_points/num_grades
			if avg_grade >= 98.5:
				writer.writerow([name, round(avg_grade, 3), 'A+'])
			elif avg_grade >= 95 and avg_grade < 98.5:
				writer.writerow([name, round(avg_grade, 3), 'A'])
			elif avg_grade >= 91.5 and avg_grade < 95:
				writer.writerow([name, round(avg_grade, 3), 'A-'])
			elif avg_grade >= 88.5 and avg_grade < 91.5:
				writer.writerow([name, round(avg_grade, 3), 'B+'])
			elif avg_grade >= 85 and avg_grade < 88.5:
				writer.writerow([name, round(avg_grade, 3), 'B'])
			elif avg_grade >= 81.5 and avg_grade < 85:
				writer.writerow([name, round(avg_grade, 3), 'B-'])	
			elif avg_grade >= 78.5 and avg_grade < 81.5:
				writer.writerow([name, round(avg_grade, 3), 'C+'])
			elif avg_grade >= 75 and avg_grade < 78.5:
				writer.writerow([name, round(avg_grade, 3), 'C'])
			elif avg_grade >= 71.5 and avg_grade < 75:
				writer.writerow([name, round(avg_grade, 3), 'C-'])
			elif avg_grade >= 68.5 and avg_grade < 71.5:
				writer.writerow([name, round(avg_grade, 3), 'D+'])
			elif avg_grade >= 65 and avg_grade < 68.5:
				writer.writerow([name, round(avg_grade, 3), 'D'])
			elif avg_grade >= 61.5 and avg_grade < 65:
				writer.writerow([name, round(avg_grade, 3), 'D-'])
			elif avg_grade < 61.5:
				writer.writerow([name, round(avg_grade, 3), 'F'])
		except ZeroDivisionError:
			writer.writerow([name, 'N/A', 'N/A'])



			








