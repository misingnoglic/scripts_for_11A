import csv

group_placement = open("group_placement_updated.csv")
grades = open("grading.csv")

already_placed = set()
all_students = set()
name = {}

for line in csv.DictReader(group_placement):
	already_placed.add(line['email'])

for line in csv.DictReader(grades):
	all_students.add(line['Email address'])
	name[line['Email address']] = "{}, {}".format(line['First name'], line['Last name'])

new_students = all_students-already_placed

new_students_file = open("new_students.txt", "w")
for student in new_students:
	new_students_file.write("{}\t{}\n".format(student, name[student]))
new_students_file.close()
