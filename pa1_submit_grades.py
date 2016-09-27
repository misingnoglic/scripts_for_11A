import csv

def int_or_zero(x):
	if x: return int(x)
	else: return 0

with open("pa1_completed_grades.csv") as grade_file:
	grade_csv = csv.DictReader(grade_file)
	grade_field  = "Assignment:Programming Assignment 1 (Percentage)"
	feedback_field = "Assignment:Programming Assignment 1 (Feedback)"
	arya_cal_url = "https://calendar.google.com/calendar/selfsched?sstoken=UUN4TVU3ZTdsX0J4fGRlZmF1bHR8NGIwY2UyMjA2ODQ5NjE0YjJjOWIyYWJiMTNiNDRiYzM"
	fieldnames = ["First name", "Last name", "ID", "Email address", grade_field, feedback_field]
	new_grade_file = open("pa1_formatted_grades.csv", 'w')
	new_grade_csv = csv.DictWriter(new_grade_file, fieldnames)
	new_grade_csv.writeheader()
	current_ta = ""
	for line in grade_csv:
		if line["TA"]: 
			current_ta = line["TA"]
			if current_ta == "Done": print "Done";break
			continue
		#print line
		external_score = line["External Score (max 40)"]
		internal_score = line["Internal Score (max 60)"]
		main_method_print_reduction = line["Main Method Print Reduction (max 5)"]
		header_deduction = line["Header Deduction (max 5)"]
		comments_deduction = line["Comments Deductions (max 10)"]
		bad_indentation_deduction = line["Bad Indentation Deduction (max 10)"]
		weird_spacing_deduction = line["Weird Spacing Deduction (max 5)"]
		bad_name_deduction = line["Bad Method Name Deduction (max 10)"]
		disorganized_deduction = line["Disorganized Code Deduction (max 3)"]
		incorrect_name_deduction = line["Incorrect File Name (3)"]

		external_comments = line["External Comments"]
		internal_comments = line["Internal Code Comments"]
		additional_comments = line["Additional Comments"]
		didnt_compile = line["Didn't Compile"]

		first_name = line["First name"]
		last_name = line["Last name"]
		id_num = line["ID number"]
		email = line["Email address"]


		deductions = [int_or_zero(x) for x in 
			[main_method_print_reduction,
				header_deduction,
				comments_deduction, 
				bad_indentation_deduction, 
				weird_spacing_deduction,
				bad_name_deduction,
				disorganized_deduction, 
				incorrect_name_deduction]] 
		deduction_names = ["Printing in main method", "Missing elements of header", "No comments", "Bad indentation", "Bad spacing", "Bad naming of methods", "Disorganized code", "Incorrect file name"]
		total_score = int_or_zero(external_score) + int_or_zero(internal_score) - sum(deductions)
		assert(total_score == int(line[grade_field]))
		assert(current_ta)

		overall_comments = []
		overall_comments.append("Graded by {}".format(current_ta))
		overall_comments.append(" - ")
		overall_comments.append("External score: {}/40".format(int_or_zero(external_score)))
		if external_comments:
			overall_comments.append("External score comments:")
			overall_comments.append(external_comments)
		overall_comments.append(" - ")
		overall_comments.append("Internal score: {}/60".format(int_or_zero(internal_score)))	
		student_deductions = [(x,y) for (x,y) in zip(deductions, deduction_names) if x>0]
		if student_deductions: 
			overall_comments.append("Deductions:")
			for x,y in student_deductions: 
				overall_comments.append("{}: -{}".format(y,x))
		if internal_comments:
			overall_comments.append(" - ")
			overall_comments.append("Internal score comments: ")
			overall_comments.append(internal_comments)
		if additional_comments:
			overall_comments.append(" - ")
			overall_comments.append("Additional comments: ")
			overall_comments.append(additional_comments)
		overall_comments.append(" - ")
		overall_comments.append("Total score: {}/100".format(total_score))
		
		overall_comments = "\n".join(overall_comments)
		
		if didnt_compile:
			overall_comments = "This assignment recieved a zero, as the submission on Latte did not compile. If you would like to meet with Arya to show him that you can fix the error, you can make an appointment to recieve your points back: {}".format(arya_cal_url)
			total_score = 0
		
		new_grade_csv.writerow({"First name":first_name, "Last name":last_name, "ID":id_num, "Email address":email, grade_field:total_score, feedback_field:overall_comments})

new_grade_file.close()

		
		
		
		
