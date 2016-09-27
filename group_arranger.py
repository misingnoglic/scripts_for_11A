from collections import Counter
try:
	from tabulate import tabulate
except:
	# If you don't have the package, I made my own version of tabulate for this specific use case
	def tabulate(list_of_dicts, *args, **kwargs):
		for k,v in list_of_dicts:
			print "{}\t{}".format(k,v)

import csv
try:
	from wc_gen import make_wordcloud
except:
	# Don't throw a fit if wordclouds can't be made
	def make_wordcloud(*args, **kwargs): print "Could not make wordcloud"

"""
This program reads a file, which is a list of Python lists
The first element of the list is the student's email
The rest of the list is all of the categories the student is in.
There is probably a better way to organize it (like not include the letters)

It also reads 

An example would be like this
['aboudaie@brandeis.edu', 'A1', 'B4', 'C2', 'D2', 'E1', 'F0']
['arya@brandeis.edu', 'A2', 'B2', 'C1', 'D2', 'E3', 'F1']

The program then assigns them to the correct groups, and writes those groups to a CSV
It also prints out some statistics, and generates word charts.

With little modifications, I used this code to explore and count the data as well.
"""

categories = raw_input("Name of file with categories: ")
f = open(categories).read().splitlines()
f2 = open('group_placement.csv', 'w')
answers = open(raw_input("Name of CSV file with answers: "))



groups = [[] for x in range(13)]  # Will contain each email in the index of the group they are in

people = {}
people2 = {}

for line in list(csv.reader(answers)):
	people[line[1]] = line[:7] # Matches email to survey answers

for line in f:
	l = eval(line)
	people2[l[0]] = l[1:] # Matches email to group


for line in f:
	l = eval(line) # turns string into python list
	email = l[0]
	if "D1" in l:  # 1. All Female Group - D1 in list
		groups[0].append(email)
	else:
		if "A3" in l:  # 2. All "Want to see what CS is" - A3 in list
			groups[1].append(email)
		elif "A1" in l:  # Want to Major - A1
			if "C2" in l:  # No Experience - C2

				# # # 3. High School Math - B3
				if "B2" in l or "B3" in l: groups[2].append(email)
				# # # 4. Brandeis Calculus - B4
				elif "B4" in l: groups[3].append(email)
				# # # 5. Higher than Calc - B1
				elif "B1" in l: groups[4].append(email)
				
				 # I want to make sure everyone is grouped - so if a name is printed there is an error
				else: print line
			elif "C1" in l: # # Some Experience - C1
				if "F5" in l: groups[5].append(email) # # # 8. All questions right - F5

				# The code uses this "intersection" thing a lot - 
				# I am basically checking if F4, F3, or F2 are in the list

				# # # 7. Answered some Qs correctly - F1-4
				elif len(set(l).intersection({"F4", "F3", "F2"}))>0: groups[6].append(email)
				else: print line  # Not matched
		
		# Mix with skills - A2,4-6
		elif len(set(l).intersection({"A2", "A4", "A5", "A6"}))>0:
			if "C1" in l: # # Experience - C1
				if "F5" in l: groups[7].append(email)  # # # 8. All questions right - F5
				
				# # # 9. Some questions right - F1-F4
				elif len(set(l).intersection({"F4", "F3", "F2", "F1"}))>0:
					groups[8].append(email)
				else:  # Not matched
					print line
			elif "C2" in l:  # # No Experience - C2
				if "A5" in l: groups[9].append(email) # # # 10. Want to mix with discipline - A5
				elif "A6" in l: groups[10].append(email)# # # 11. Might major in CS - A6
				elif "A4" in l: # # # Just because - A4
					if "B1" in l or "B4" in l: # # # # 12. Brandeis Math - B1, B4
						groups[11].append(email)
					elif "B2" or "B3" in l: # # # # 13. High school math B2, B3
						groups[12].append(email)
					else: print line
				else: print line
			else: print line
		else: print line


# Displays table of how many are in each group (can be modified easily  to show other things)

def combine(L): return reduce(lambda x,y:x+y, L) # way to merge list of lists	

#List of counters for each category (weird syntax I'm sorry)
categories_counter = [Counter(x) for x in (zip(*[people2[x] for x in combine(groups)]))]

# Prints that list better
for d in categories_counter:
	if d:
		print tabulate([ [k,v] for k,v in d.viewitems() ])
		print ""

words = [] # List of all words for "Why CS" question
# This can be modified easily to make several wordclouds, or only include 
i = 0
while i<len(groups):
	words += [people[p][2] for p in groups[i]]
	i+=1
make_wordcloud("\n".join(words), "wordcloud"+".png")

i = 0
f2.write("email,group_num\n")
while i<len(groups):
	for person in groups[i]:
		f2.write("{},{}\n".format(person,i+1))
	i+=1
f2.close()


print [len(x) for x in groups]
			

# 1. All Female Group - D1 in list
# 2. All "Want to see what CS is" - A3 in list

# Want to Major - A1
# # No Experience - C2
# # # 3. High School Math - B3
# # # 4. Brandeis Calculus - B4
# # # 5. Higher than Calc - B1

# # Some Experience - C1
# # # 6. Answered all Qs correctly - F5
# # # 7. Answered some Qs correctly - F1-4

# Mix with skills - A2,4-6
# # Experience - C1
# # # 8. All questions right - F5
# # # 9. Some questions right - F1-F4

# # Not Experience - C2
# # # 10. Want to mix with discipline - A5
# # # 11. Might major in CS - A6
# # # Just because - A4
# # # # 12. Brandeis Math - B1, B4
# # # # 13. High school math B2, B3
