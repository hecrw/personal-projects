class Employee:
    employee_dict = {}

    def add_emp(self, name, age, salary):
        self.employee_dict[name] = {"name": name, "age": age, "salary": salary}

    def print_emp(self):
        if self.employee_dict:
            print("Employee list :")
            for i in self.employee_dict.keys():
                print(f"{i['name']} is {i['age']} years old and their salary is {i['salary']}")
        else:
            print("There are no current employees!")

    def delete_age(self, start, end):
        h = []
        if self.employee_dict:
            for i in self.employee_dict.values():
                if start <= i['age'] <= end:
                    h.append(i['name'])
            if h:
                for i in h:
                    print("Deleting:", i)
                    del self.employee_dict[i]
            else:
                print("Invalid age range")
        else:
            print("List is empty!")


x = 0
e = Employee()
while x != 5:
    try:
        x = int(input("Enter your choice:\n1)Add new employee\n2)Print all employee\n3)Delete by age\n4)Update salary by name\n5)End your program\nEnter your choice from 1 to 5 :"))
        if x < 1 or x > 5:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue
    if x == 1:
        print("Enter employee data :")
        try:
            n = input("Enter the name :")
            a = int(input("Enter their age :"))
            s = int(input("Enter their salary :"))
            if not isinstance(s, int) or not isinstance(a, int):
                raise ValueError("Invalid input")
            e.add_emp(n, a, s)
        except ValueError as err:
            print(err)
            continue
    if x == 2:
        e.print_emp()
    if x == 3:
        try:
            n = int(input("Enter the start of your age range :"))
            t = int(input("Enter the end :"))
            if not isinstance(n, int) or not isinstance(t, int):
                raise ValueError("Invalid input: age range must be integers")
            e.delete_age(n, t)
        except ValueError as err:
            print(err)
            continue
    if x == 4:
        n = input("Enter the name of the employee :")
        if n not in e.employee_dict:
            print("Doesnt exist")
        else:
            s = int(input("Enter the new salary :"))
            e.employee_dict[n]["salary"] = s
    if x == 5:
        break
print("End of program.")
