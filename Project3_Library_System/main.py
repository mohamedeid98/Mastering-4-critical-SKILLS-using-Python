def input_valid_int(msg, start = 0, end = None):
    while True:
        inp = input(msg)
        if inp.isdecimal():
            if start == 0 and end == None:
                return int(inp)
            elif start <= int(inp) <= end:
                return int(inp)
            else:
                print('Invalid range. Try again!')
        else:
            print('Invalid input. Try again!')

class Book:
    def __init__(self, name, id, quantity):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.available = quantity

    def __str__(self):
        return f'Book Name: {self.name}, Book id: {self.id}, Available: {self.available}'

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = {}

    def __str__(self):
        return f'User name: {self.name}\tid: {self.id}'


class Library:
    def __init__(self):
        self.users = []
        self.books = []
        self.search_prefix = {}
    
    def add_book(self):
        print('\nEnter book info: ')
        name = input('Enter book name: ')
        id = input_valid_int('Enter book id: ')
        quantity = input_valid_int('Enter book quantity: ')
        new_book = Book(name, id, quantity)
        self.books.append(new_book)
        self.update_prefix(name)

    def update_prefix(self, book_name):
        for idx in range(len(book_name)):
            prefix = book_name[:idx+1]
            self.search_prefix.setdefault(prefix, [])
            self.search_prefix[prefix].append(book_name)


    def add_user(self):
        print('Enter user info: ')
        name = input('Enter user name: ')
        id = input_valid_int('Enter user id: ')
        new_user = User(name, id)
        self.users.append(new_user)


    def print_books(self):
        for book in self.books:
            print()
            print(book)
    
    
    def print_by_prefix(self):
        prefix = input('Enter prefix: ')
        print(self.search_prefix[prefix])


    def borrow(self):
        trials = 3
        flag = False
        while trials:
            username = input('\nEnter user name: ')
            for user in self.users:
                if user.name == username:
                    flag = True
                    break
            if flag:
                break
            print('Invalid user name, please try agian')
            trials -= 1
        if flag:
            book_name = input('Enter book name: ')
            if self.search_prefix.get(book_name, 0):
                for book in self.books:
                    if book.name == book_name:
                        book.available -= 1
                        user.borrowed_books.setdefault(book.id, book.name)
            else:
                print('Error! No such book name')

        else:
            print('Trials limit reached')


    def print_users_borrowed_books(self):
        for user in self.users:
            if user.borrowed_books:
                print(user)
                print('Borrowed books: ')
                for key, val in user.borrowed_books.items():
                    print(f'Book name: {val}, id: {key}')

             


class LibraryManager:
    def __init__(self):
        self.library = Library()
    
    def print_menu(self):
        print('\nProgram Options:')
        options = [
            '1) Add book',
            '2) Print library books',
            '3) Print books by prefix',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users',
            '9) End program'

        ]
        print('\n'.join(options))
        msg = F'Enter your choice (from 1 to 9): '
        return input_valid_int(msg, 1, 9)
    

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.library.add_book()
            elif choice == 2:
                self.library.print_books()
            elif choice == 3:
                self.library.print_by_prefix()
            elif choice == 4:
                self.library.add_user()
            elif choice == 5:
                self.library.borrow()
            elif choice == 6:
                ...
            elif choice == 7:
                self.library.print_users_borrowed_books()
            elif choice == 8:
                ...
            else:
                break


app = LibraryManager()
app.run()