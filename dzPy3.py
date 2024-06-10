# class Command:
#     def execute(self):
#         pass
#
#
# class ConcreteCommandA(Command):
#     def __init__(self, receiver):
#         self.receiver = receiver
#
#     def execute(self):
#         self.receiver.action_a()
#
#
# class ConcreteCommandB(Command):
#     def __init__(self, receiver):
#         self.receiver = receiver
#
#     def execute(self):
#         self.receiver.action_b()
#
#
# class Receiver:
#     def action_a(self):
#         print("Receiver executing action A")
#
#     def action_b(self):
#         print("Receiver executing action B")
#
#
# class Invoker:
#     def __init__(self):
#         self.commands = []
#
#     def add_command(self, command):
#         self.commands.append(command)
#
#     def execute_commands(self):
#         for command in self.commands:
#             command.execute()
#
#
# receiver = Receiver()
# command_a = ConcreteCommandA(receiver)
# command_b = ConcreteCommandB(receiver)
# invoker = Invoker()
#
# invoker.add_command(command_a)
# invoker.add_command(command_b)
# invoker.execute_commands()


# from abc import ABC, abstractmethod
#
#
# class NumberSetInterface(ABC):
#     @abstractmethod
#     def get_numbers(self):
#         pass
#
#
# class NumberSet(NumberSetInterface):
#     def __init__(self, filename):
#         self.filename = filename
#         self.numbers = []
#
#     def get_numbers(self):
#         with open(self.filename, 'r') as file:
#             self.numbers = [int(line.strip()) for line in file.readlines()]
#         return self.numbers
#
#     def update_numbers(self):
#         pass
#
#
# class NumberSetProxy(NumberSetInterface):
#     def __init__(self, number_set):
#         self.number_set = number_set
#
#     def get_numbers(self):
#         numbers = self.number_set.get_numbers()
#         with open('log.txt', 'a') as log_file:
#             log_file.write(f"Accessed numbers: {numbers}\n")
#         return numbers
#
#
# number_set = NumberSet('numbers.txt')
# proxy = NumberSetProxy(number_set)
#
# numbers = proxy.get_numbers()
# print(numbers)


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#
# class Librarian:
#     _instance = None
#
#     @classmethod
#     def get_instance(cls):
#         if not cls._instance:
#             cls._instance = Librarian()
#         return cls._instance
#
#
# class Reader:
#     def __init__(self, name):
#         self.name = name
#
#
# class BookFactory:
#     def create_book(self, title, author, book_type):
#         if book_type == "fiction":
#             return FictionBook(title, author)
#         elif book_type == "science":
#             return ScienceBook(title, author)
#
#
# class BookNotifier:
#     def update(self, book):
#         print("New book available: {} by {}".format(book.title, book.author))
#
#
# class Command:
#     def execute(self):
#         pass
#
#
# class AddBookCommand(Command):
#     def __init__(self, book):
#         self.book = book
#
#     def execute(self):
#         Library.add_book(self.book)
#
#
# class SearchStrategy:
#     def search(self, query):
#         pass
#
#
# class TitleSearchStrategy(SearchStrategy):
#     def search(self, query):
#         return [book for book in Library.books if query in book.title]

