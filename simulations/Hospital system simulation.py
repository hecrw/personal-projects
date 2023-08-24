import json


class Patient:
    patients = {}

    def add_patient(self, name, status, sps):
        status1 = ""
        if status == 0:
            status1 = "normal"
        if status == 1:
            status1 = "urgent"
        if status == 2:
            status1 = "super urgent"
        self.patients[name] = {"patient's name": name, "status": status1, "specialization": sps}
        return name, status

    def remove_patient(self, name):
        v = self.patients[name]["specialization"]
        del self.patients[name]
        print("patient has been removed successfully")
        return v

    def prints(self):
        print(json.dumps(self.patients, indent=4))


Queue = []
specialization = {}
for i in range(1, 21):
    key = i
    specialization[key] = 0
print("Program options:\n1)Add new patient\n2)Print all patients\n3)Get next patient\n4)Remove a leaving patient")
print("5)End the program")
x = 0
p = Patient()
while x != 5:
    try:
        x = int(input("Enter your choice (from 1 to 5):"))
        if x < 1 or x > 5:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue
    if x == 1:
        try:
            n = input("Enter the patients name :")
            sp = int(input("Enter the specialization [1-20] :"))
            if sp < 1 or sp > 20:
                raise ValueError
            s = int(input("Enter their status 0:(Normal), 1:(Urgent), 2(Super urgent) :"))
            if s < 0 or s > 2:
                raise ValueError
            if specialization[sp] > 10:
                print("This speciality is currently full!")
            else:
                specialization[sp] += 1
                Queue.append(p.add_patient(n, s, sp))
                Queue = sorted(Queue, key=lambda m: m[1], reverse=True)
        except ValueError:
            print("invalid!")
            continue
    if x == 2:
        if p.patients:
            p.prints()
        else:
            print("There are no current patients")
    if x == 3:
        try:
            io = int(input("Enter the specialization: "))
            if io < 1 or io > 20:
                raise ValueError
            elif specialization[io] == 0:
                print("There are no patients in this current specialization")
            else:
                found = False
                for status in [2, 1, 0]:
                    for i, (name, s) in enumerate(Queue):
                        if s == status and p.patients[name]["specialization"] == io:
                            print(
                                f"Next patient is: {name} ({'super urgent' if status == 2 else 'urgent' if status == 1 else 'normal'})")
                            Queue.pop(i)
                            specialization[io] -= 1
                            found = True
                            del p.patients[name]
                            if found:
                                break
                        if found:
                            break
        except ValueError:
            print("Invalid!")
            continue
    if x == 4:
        n = input("Enter the name of the patient you want to remove :")
        if Queue:
            for i in Queue:
                if n in i:
                    Queue.remove(i)
                    specialization[p.remove_patient(n)] -= 1
                elif n not in i:
                    print("Patient not found")
        else:
            print("Queue is empty")
    if x == 5:
        print("Program has been terminated")


