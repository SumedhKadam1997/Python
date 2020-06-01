import csv
import os


def add_patient():
    name = input("What is the name of patient ? ")
    age = input("What is the age ? ")
    illness = input("What is the illness ? ")
    prev_treatments = input("What are the previous treatments given ? ")
    with open ("patients.csv","a+") as f:
        new_patient = csv.writer(f)
        new_patient.writerow([name]+[age]+[illness]+[prev_treatments])

def show_patient():
    with open("patients.csv","r") as f:
        data = csv.reader(f)
        for row in data:
            print(", ".join(row))

first = input("Are you opening for first time ? (y/n) ")
if first == 'y':
    os.remove("patients.csv")
    with open ("patients.csv","a+") as f:
        new_patient = csv.writer(f)
        new_patient.writerow(['Name']+['Age']+['Illness']+['Previous Treatments'])

else:
    pass

while True:
    condi = input("Which operation would you like to perform ? \nTo Add new patient press 1\nTo show all patients press 2\nTo exit press 3 ")

    if condi == "1":
        add_patient()
    elif condi == "2":
        show_patient()
    elif condi == "3":
        break