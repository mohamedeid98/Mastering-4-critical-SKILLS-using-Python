def input_valid_int(msg, start = 0, end = None):
    # keep iterating till the given input is valid
    # hidden assumption: both start and end either value or none. That is bad
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee: {self.name} has age {self.age} and salary {self.salary}'

class EmployeesManager:
    def __init__(self):
        self.employees = []
    
    def add_employee(self):
        print('Enter employee data:')
        name = input('Enter the name: ')
        age = input_valid_int('Enter the age: ')
        salary = input_valid_int('Enter the salary: ')
        emp = Employee(name, age, salary)
        self.employees.append(emp)

    def list_employees(self):
        print('**Employees List**')
        for emp in self.employees:
            print(emp)

    def del_ages(self):
        age_from = input_valid_int('Enter age from: ')
        age_to = input_valid_int('Enter age to: ')
  
        self.employees = [emp for emp in self.employees if not age_from <= emp.age <= age_to]
        print('Deleted successfully')

    def update_salary(self):
        name = input('Enter name:')
        found = False
        for emp in self.employees:
            if emp.name == name:
                emp.salary = input_valid_int('Enter new salay: ')
                found = True
        if not found:
            print('Error: No employee with such a name')
        
        
class FrontEndManager:
    def __init__(self):
        self.man = EmployeesManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.man.add_employee()
            elif choice == 2:
                self.man.list_employees()
            elif choice == 3:
                self.man.del_ages()
            elif choice == 4:
                self.man.update_salary()
            else:
                break


if __name__ == '__main__':
    app = FrontEndManager()
    app.run()