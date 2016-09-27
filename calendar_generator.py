import csv
date = "09/{}/2016"
convert = {"Sunday": "04", "Monday": "05", "Tuesday": "06", "Wednesday": "07", "Thursday": "08", "Friday": "09", "Saturday": "10"} 

new_form = open("AllOfficeHours2.csv", 'w')
fieldnames = ["Subject", "Start Date", "Start Time", "End Time", "All Day Event", "Description", "Location", "Private"]
description = """Time: {}
Office hours for {} held in the Vertica Lounge
Picture: {}
Email: {}"""
location = "Vertica Lounge"
subject = "{} p:{} old:{}"

writer = csv.DictWriter(new_form, fieldnames=fieldnames)
writer.writeheader()

with open("oo_form.csv") as form:
    form_csv = csv.DictReader(form)
    for line in form_csv:
        name = line["What is your name?"]
        email = line['Username']
        picture = line['Link to a picture of yourself.']
        new_ta = line['Have you TAd for COSI 11A before?']
        times = line['Times you are available'].splitlines()
        for time in times:
            priority, day, hour = time.split(" ")
            priority = priority[:1]
            day = day.strip(",")
            start, end = hour.split("-")
            start = start[:-2]+" "+start[-2:]
            end = end[:-2]+" "+end[-2:]
            day = date.format(convert[day])
            writer.writerow({"Subject":subject.format(name, priority, new_ta), "Start Date":day, "Start Time":start, "End Time":end, "All Day Event":"False", "Description":description.format(hour, name, picture, email), "Location":location, "Private":"False"})

    new_form.close()
