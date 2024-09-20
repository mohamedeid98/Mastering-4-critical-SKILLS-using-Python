status_code = ['Normal', 'Urgent', 'Super Urgent']

def input_valid_int(msg, start=0, end=None):
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


def status_based_add_sort(queue, item):
    if item.status == 0 or len(queue) == 0:
        queue.append(item)

    elif item.status == 1:
        for idx, pa in enumerate(queue):
            if pa.status == 0:
                queue.insert(idx, item)
                break

    elif item.status == 2:
        for idx, pa in enumerate(queue):
            if pa.status == 1:
                queue.insert(idx, item)
                break

class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status


class Specialization:
    def __init__(self, number):
        self.queue = []
        self.max_len = 10
        self.curr = 0
        self.specN = number

    def is_full(self):
        return self.curr >= self.max_len

    def add_patient(self, name, status):
        if not self.is_full():
            patient = Patient(name, status)
            status_based_add_sort(self.queue, patient)
            self.curr += 1
        else:
            print('\nSorry, we can not add more patients for this specialization at the moment.')

    def get_next(self):
        if self.curr == 0:
            print('\nNo waiting patients')

        else:
            print(f'\n{self.queue[0].name}, your turn')
            del self.queue[0]
            self.curr -= 1

    def remove_patient(self, name):
        flag = False
        for idx, pa in enumerate(self.queue):
            if pa.name == name:
                flag = True
                break
        if flag:
            del self.queue[idx]
            self.curr -= 1
            print('\nRemoved successfully!')
        else:
            print('\nNo patient with such a name in this specialization!')

    def print_all(self):
        print(f'Specialization {self.specN}: There are {self.curr} patients')
        for pa in self.queue:
            print(f'Patient: {pa.name} is {status_code[pa.status]}')


class SpecializationsManager:
    def __init__(self):
        self.specializations = []
        for i in range(0, 20):
            spec = Specialization(i+1)
            self.specializations.append(spec)

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new patient',
            '2) List all patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                specN = input_valid_int('Enter specialization: ', 1, 20)
                name = input('Enter patient name: ')
                status = input_valid_int('Enter status(0 normal/ 1 urgent / 2 super urgent): ', 0, 2)
                self.specializations[specN-1].add_patient(name, status)

            elif choice == 2:
                for spec in self.specializations:
                    spec.print_all()

            elif choice == 3:
                specN = input_valid_int('Enter specialization: ', 1, 20)
                self.specializations[specN-1].get_next()

            elif choice == 4:
                specN = input_valid_int('Enter specialization: ', 1, 20)
                name = input('Enter patient name: ')
                self.specializations[specN-1].remove_patient(name)

            else:
                break


app = SpecializationsManager()
for i in range(20):
    for j in range(10):
        app.specializations[i].add_patient('dummy', j%3)
app.run()