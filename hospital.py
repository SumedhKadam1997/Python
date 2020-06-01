patients = {}
def add_patient():
    name = input("What is the name of patient ? ")
    age = input("What is the age ? ")
    illness = input("What is the illness ? ")
    prev_treatments = input("What are the previous treatments given ? ")
    patients[name]={'age':age}
    patients[name].update(illness=illness)
    patients[name].update(previous_treatments=prev_treatments)
    cond = input("Would you like to add a new patient ? (y/n) ")
    if cond == 'y':
        add_patient()
    else:
        pass

    return patients



def show_patients():
    names = patients.keys()
    for i in names:
        print(">>  "+i)


to_do = input("What would like you to do ?\n(Add new patient / Show existing patients)\nTo add new patient select 1\nTo show patients select 2 ")
if to_do == '1':
    add_patient()
elif to_do == '2':
    show_patients()
else:
    pass