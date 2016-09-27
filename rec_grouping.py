import csv
with open("rec.csv",'r') as f:
	with open("groups.txt",'a') as out:
		students = csv.reader(f)
		letters = ["ABCDEFGHIJ"]
		numbers = ["123"]
		records = []
		for line in list(students)[1+108:]:
			record = []
			record.append(line[1])
			print line[2] # Why CS
			cat = raw_input("group: ")
			record.append("A"+cat)
			
			print line[3] # Math Class
			cat = raw_input("group: ")
			record.append("B"+cat)

			# Math Class
			if line[4]=="Yes": cat = "1"
			else: cat = "2"
			record.append("C"+cat)

			if line[5]=="All Woman/non-binary group": cat = "1"
			else: 
				cat = "2"
			record.append("D"+cat)
			
			if line[6]=="": cat = "1"
			else:
				print line[6]
				cat = raw_input("group: ")
			record.append("E"+cat)
			
			total_score = 0
			for i in range(7,12):
				if line[i]=="": score1 = 0
				else:
					print line[i]
					score = int(raw_input("score: "))
					total_score+=score
				
			record.append("F"+str(total_score))
			out.write(str(record)+"\n")
			records.append(record)
