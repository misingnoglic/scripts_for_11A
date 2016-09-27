import csv
import operator 
students = csv.DictReader(open("all_grades.csv"))
tas = csv.DictReader(open("ta_cant_grade.csv"))
fieldnames = ['TA', 'First Name', 'Last Name', 'Email']
grade_file = open("pa2_grade_sheet.csv", 'w')
grade_sheet = csv.DictWriter(grade_file, fieldnames = fieldnames)

ta_list = []
cant_grade = {}
grading_list = {}
student_info = {}

student_list = []

num = [19,19,19]

for t in tas:
	ta_list.append(t['Username'])
	cant_grade[t['Username']] = []
	for email in t["What are the emails of the people you don't want to grade? (separated by a space). "].split():
		cant_grade[t['Username']].append(email)

ta_list = ta_list[1:]+[ta_list[0]]

for s in students:
	student_list.append(s['Email address'])
	student_info[s['Email address']] = [s['First name'], s['Last name']]

graders = []

offset=0
for (i, t) in enumerate(ta_list):
	n = num[i%3]
	graders += [[]]
	for s in student_list[offset:offset+n]:
		graders[i].append(s)
		#if s in cant_grade[t]:
		#	print s,t
	#print t,student_list[offset]
	offset += n

#print graders
#print [len(x) for x in graders]

for i, ta in enumerate(graders):
	for student in ta:
		if student in cant_grade[ta_list[i]]:
			#print ta_list[i], student
			if len(graders[-1])<19 and student not in cant_grade[ta_list[-1]]:
				graders[-1].append(student)
				graders[i].remove(student)
			else:
				replacement_found = False
				while not replacement_found:
					ta_offset = 1
					if student not in cant_grade[ta_list[(i+ta_offset)%len(ta_list)]]:
						for replacement_student in graders[i+ta_offset]:
							if replacement_student not in cant_grade[ta_list[i]]:
								graders[i].remove(student)
								graders[i].append(replacement_student)
								graders[(i+ta_offset)%len(ta_list)].remove(replacement_student)
								graders[(i+ta_offset)%len(ta_list)].append(student)
								replacement_found = True
								break
					else: 
						ta_offset +=1

print [len(x) for x in graders]
combined = reduce(operator.add, graders)
assert len(combined) == len(set(combined)) ==len(student_list)
grade_sheet.writeheader()
for i, ta in enumerate(graders):
	for student in ta:
		grade_sheet.writerow({'TA':ta_list[i], 'First Name':student_info[student][0], 'Last Name':student_info[student][1], 'Email': student})

grade_file.close()
