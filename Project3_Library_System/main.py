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


    def borrow(self):
        if self.available > 0:
            self.available -= 1
            return True
        else:
            return False
        

    def return_copy(self):
        if self.available < self.quantity:
            self.available += 1


    def __str__(self):
        return f'Book Name: {self.name}, Book id: {self.id}, Available: {self.available}'



class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []


    def borrow(self, book):
        self.borrowed_books.append(book)


    def is_borrowed(self, book):
        for mybook in self.borrowed_books:
            if mybook.id == book.id:
                return True
        return False
    

    def return_copy(self, book):
        for idx, mybook in enumerate(self.borrowed_books):
            if mybook.id == book.id:
                del self.borrowed_books[idx]
                break


    def __str__(self):
        return f'User name: {self.name}\tid: {self.id}'


class Library:
    def __init__(self):
        self.users = []
        self.books = []
        self.search_prefix = {}
    
    def add_book(self, name, id, copies):
        self.books.append(Book(name, id, copies))
        self.update_prefix(name)

    def update_prefix(self, book_name):
        for idx in range(len(book_name)):
            prefix = book_name[:idx+1]
            self.search_prefix.setdefault(prefix, [])
            self.search_prefix[prefix].append(book_name)


    def add_user(self, name, id):
        self.users.append(User(name, id))

    
    def get_books_with_prefix(self, prefix):
        return self.books if prefix == '' else self.search_prefix[prefix]
    

    def get_user_by_name(self, username):
        for usr in self.users:
            if usr.name == username:
                return usr
        return None


    def get_book_by_name(self, bookname):
        for mybook in self.books:
            if mybook.name == bookname:
                return mybook
        return None


    def borrow(self, username, bookname):
        book = self.get_book_by_name(bookname)
        user = self.get_user_by_name(username)

        if book == None or user == None:
            return False
        if book.borrow():
            user.borrow(book)
            return True
        return False
    

    def return_copy(self, username, bookname):
        book = self.get_book_by_name(bookname)
        user = self.get_user_by_name(username)

        if book == None or user == None:
            return

        if user.is_borrowed(book):
            user.return_copy(book)
            book.return_copy()
            return 1
        else:
            return -1


    def print_users_borrowed_book(self, bookname):
        book = self.get_book_by_name(bookname)
        if book == None:
            return []
        
        return [usr for usr in self.users if usr.is_borrowed(book)]
             

    def print_users(self):
        return self.users


class FrontEnd:
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
    

    def add_book(self):
        print('\nEnter book info:')
        name = input('Enter book name: ')
        id = input_valid_int('Enter book id: ')
        numberOfcopies = input_valid_int('Enter number of copies: ')
        self.library.add_book(name, id, numberOfcopies)


    def print_books(self):
        self.print_name_prefix(just_print_all=True)


    def print_name_prefix(self, just_print_all=False):
        prefix = ''
        if not just_print_all:
            prefix = input('Enter prefix: ')

        books = self.library.get_books_with_prefix(prefix)
        if not prefix:
            books_str = '\n'.join([str(book) for book in books])
            print(books_str)
        else:
            print(books)


    def add_user(self):
        print('\nEnter user info:')
        name = input('Enter user name: ')
        id = input_valid_int('Enter user id: ')
        self.library.add_user(name, id)


    def get_inputs_with_trials(self, max_trials=3):
        while max_trials > 0:
            max_trials -= 1
            user = self.library.get_user_by_name(input('Enter user name: '))
            if user is None:
                print('Invalid user name!')
                continue

            book = self.library.get_book_by_name(input('Enter book name: '))
            if book is None:
                print('Invalid book name!')
                continue

            return user.name, book.name

        print('You did several trials! Try again later.')
        return None, None
    

    def borrow(self):
        username, bookname = self.get_inputs_with_trials()

        if username and bookname:
            if not self.library.borrow(username, bookname):
                print('Failed to borrow the book!')


    def return_copy(self):
        username, bookname = self.get_inputs_with_trials()
        if username and bookname:
            self.library.return_copy(username, bookname)


    def print_users_borrowed_book(self):
        bookname = input('\nEnter book name: ')
        if self.library.get_book_by_name(bookname) is None:
            print('Invalid book name')
            return
        users = self.library.print_users_borrowed_book(bookname)
        if not users:
            print('No users borrowed this book')
        else:
            for user in users:
                print(user)
        

    def print_users(self):
        users = self.library.print_users()
        for user in users:
            print(user)


    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.print_name_prefix()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow()
            elif choice == 6:
                self.return_copy()
            elif choice == 7:
                self.print_users_borrowed_book()
            elif choice == 8:
                self.print_users()
            else:
                break


app = FrontEnd()
app.run()