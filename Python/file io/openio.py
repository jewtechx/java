import csv
import os

commodities = []
while True:
    commodity = input("Enter commodity: ")
    value = input("Predict stock exchange: ")


    with open("names.csv",'a') as file:
        writer = csv.DictWriter(file, fieldnames=["commodity","stock exchange"])
        writer.writerow({"commodity":commodity,"stock exchange":value})
    
    with open("names.csv") as file:
        reader = csv.DictReader(file)
        for item in reader:
            commodities.append({"commodity":item["commodity"],"stock exchange":item["stock exchange"]})

    for item in sorted(commodities,key=lambda commodity : commodity["commodity"]):
        print(f"The predicted stock exchange for {item["commodity"]} is {items["stock exchange"]}")

import csv
import os

names = []
name = input("Enter name of student ")
grade = input("Enter grade of student ")

with open('names.csv','a') as file:
    writer = csv.DictWriter(file, fieldnames=["name","grade"])
    writer.writerow({"name":name,"grade":grade})

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append({"name":row["name"],"grade":row["grade"]})

# def get_name(student):
#     return student["name"]
    

for s in sorted(names, key=lambda student : student["name"]):
    print(f"{s['name']} had grade {s['grade']}")

delete = int(input('Enter 1 to delete a file and 0 to abort '))
if delete == 1 :
    filename = input("Enter file name")
    if filename:
        reassure = input(f"Are you sure you want to delete {filename} permanently? y/n")

        if reassure == 'y':
              os.remove(filename)
              print(f'Deleted {filename} successfully')
    else:
        print('No file name given ')
else:
    print('Aborted')
