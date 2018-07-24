# Lists

enpty_list = []
empty_list2 = list()

none_list = [None] * 10

collections = ["list", "tuple", "dict", "set"]

user_data = [
    ["Elena", 4.4],
    ["Andrey", 4.2]
]

print(len(collections))

print(f"{collections[1]}")

collections[::2]

for indx, val in enumerate(collections):
    print("{} {}".format(indx, val))

print(sorted(collections))

import random

l = list()
for _ in range(10):
    l.append(random.randint(1, 20))

print(l)
# sorting in place
l.sort()
print(l)

# tuples are immutable, but elements inside the tuple are mutable
my_tuple1 = tuple(([], []))

print(f"My tuple: {my_tuple1}")
my_tuple1[0].append(2)
my_tuple1[0].append(3)
print(f"changed element inside: {my_tuple1}")

empty_dict = {}
empty_dic2 = dict()

collection_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}

print(collection_map['immutable'])

beatles_map = {'Paul': 'Bass', 'George': 'Guitar', 'John': 'Drums'}
beatles_map['Ringo'] = 'Drums'
del beatles_map['John']

beatles_map.update({'John': 'Guitar'})

print(empty_dic2.setdefault('aa', 'default'))

for key in collection_map:
    print(key)

for val in collection_map.values():
    print(val)

for key, val in collection_map.items():
    print(f"{key} {val}")

from collections import OrderedDict

ordered = OrderedDict()

for num in range(10):
    ordered[num] = str(num)

for key in ordered:
    print(key)

import this

text = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

word_dict = {}
for word in text.split():
    cleaned_word = word.strip('.,!-').lower()
    print(cleaned_word)

    if cleaned_word not in word_dict:
        word_dict[cleaned_word] = 0

    word_dict[cleaned_word] += 1

zen_items = word_dict.items()

import operator

print(sorted(zen_items, key=operator.itemgetter(1), reverse=True)[:3])

# same thing with
from collections import Counter

cleaned_list = []
for word in text.split():
    cleaned_list.append(word.strip('.,!-').lower())

print(Counter(cleaned_list).most_common(3))

num_set1 = {0, 1, 3, 5, 7, 9}
num_set2 = {2, 4, 6, 8}

num_set2.add(9)
print(f"Union: {num_set1 | num_set2}, Intersection: {num_set1 & num_set2}")

# Documentation
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/tutorial/datastructures.html
# https://en.wikipedia.org/wiki/Hash_table

# Functions

from datetime import datetime


def get_seconds():
    """Docstring example: Return number of seconds"""
    return datetime.now().second


print(f"Doc string of function {get_seconds.__name__} is \"{get_seconds.__doc__}\"")


# Example of Type Annotation in functions

def add_two(x: int, y: int) -> int:
    return x + y


res = add_two(5, 7)
print(res)


# Named arguments

def say(name, greeting):
    print(f"{greeting}, {name}!")


say(greeting="Hello", name="Kitty")


# interesting! This is Bad design
def append_one(iterable=[]):
    iterable.append(1)
    return iterable


print(append_one.__defaults__)
print(append_one())

print(append_one.__defaults__)
print(append_one())

print(append_one.__defaults__)
print(append_one())


# The fix is to use None as defaults
def append_one2(iterable=None):
    if iterable == None:
        return []
    else:
        iterable.append(1)
    return iterable


print(append_one2.__defaults__)
print(append_one2())

print(append_one2.__defaults__)
print(append_one2())

print(append_one2.__defaults__)
print(append_one2())

print(append_one2.__defaults__)
print(append_one2([1]))
print(append_one2.__defaults__)

print("-----------------------")


# The fix is to use None as defaults
def append_one3(iterable=None):
    iterable = iterable or []
    iterable.append(1)
    return iterable


print(append_one3.__defaults__)
print(append_one3())

print(append_one3.__defaults__)
print(append_one3())

print(append_one3.__defaults__)
print(append_one3())

print(append_one3.__defaults__)
print(append_one3([1]))
print(append_one3.__defaults__)


# Variable number of arguments
# Все позиционные аргументы запишутся в кортеж (tuple, immutable )args
def printer(*args):
    print(type(args))
    for a in args:
        print(a)


printer(1, 2, 3, 4, 5)
name_list = ["John", "Bill", "Amy"]
printer(*name_list)
printer(*[1, 2, 3])


# Keyword arguments, named arguments
# Все именованные аргументы запишутся в кортеж kwargs
def printer2(**kwargs):
    print(type(kwargs))

    for k, v in kwargs.items():
        print(f"{k}, {v}")


printer2(a=1, b=2)

payload = {
    'user_id': '117',
    'feedback': {'subject': 'Registration fields',
                 'message': 'There is no country for old men'}}

printer2(**payload)

printer()
printer2()

f = open("testfile.txt", "w")
f.write("This is a test file.\nInteresting example.")
f.close()

text_modes = ["r", "w", "a", "r+"]
bin_modes = ["br", "bw", "ba", "br+"]

f = open("testfile.txt", "r+")
lines = f.read()
f.tell()
f.close()
print(lines)

f = open("testfile.txt", "r+")
for line in f:
    print(f"{line}", end='')

f.seek(0)

# reading llines into a list
lines = f.readlines()
print(lines)
f.close()

# f.read() - all lines
# f.readline() - one line
# f.readlines() - all lines into a list

# Context manager can be used to avoi dclosing the file
with open("testfile.txt", "r+") as f:
    print(f.read())


# Functional Programming : Closures in our case it's n?
def func(a, b):
    return a * b


def multi(func, params):
    return func(*params)


res = multi(func, [2, 3])
print(res)


def multiply(n):
    def internal(a):
        return a * n

    return internal


multiply_by_two = multiply(2)
r = multiply_by_two(10)
print(r)

r = multiply_by_two(30)
print(r)

multiply_by_3 = multiply(3)
print(multiply_by_3(5))


# map , filter, lambda (anonymous function)

def squarify(n):
    return n * n


sq_list = list(map(squarify, range(0, 5)))
print(sq_list)


def posit(n):
    return n > 0


posit_list = list(filter(posit, range(-3, 4)))
print(posit_list)

print(type(lambda x: x ** 2))

sq_list = list(map(lambda x: x * x, range(0, 5)))
print(sq_list)

posit_list = list(filter(lambda y: y > 0, range(-3, 4)))
print(posit_list)

# list of num to list of strings with checks
num_list = [1, 3, 6, 7, 8]
# lambda z: str(z)

list_strs = list(map(lambda x: str(x), num_list))
print(f"{list_strs}")


def stringify(num_list):
    return list(map(str, num_list))


res_str_list = stringify(range(11))
print(f"{res_str_list}")

from functools import reduce


def multiply(a, b):
    return a * b


res_reduce = reduce(multiply, range(1, 6))
print(f"{res_reduce}")

# Substitute function parameter
from functools import partial


def greeter(person, greeting):
    return f"{greeting}, {person}!"


hier = partial(greeter, greeting="Hi")
helloer = partial(greeter, greeting="Hello")

print(hier("brother"))
print(helloer("sir"))

# List Comprehensions

square_list = [x ** 2 for x in range(10)]
print(square_list)

square_list2 = [x ** 2 for x in range(10) if not x % 2]
print(square_list2)

# Dictionary Comprehensions

square_map = {num: num ** 2 for num in range(5)}
print(square_map)

# Set Comprehension

reminders_set = {num % 10 for num in range(100)}
print(reminders_set)

print(type(x ** 2 for x in range(10)))

# Glue together 2 lists
zip_example = list(zip(range(10), [x * x for x in range(10)]))
print(zip_example)
print('-------------------')


# Decorators
# It's a function that take a function and returning another function
# Good thorough explanation https://gist.github.com/Zearin/2f40b7b9cfc51132851a
# Simply this
# decorated = decorator(decorated)


# Identity decorator
def decorator(func):
    return func


@decorator
def decorated():
    print("Hello!")


decorated()


def decorator2(func):
    def new_func():
        print("New func hello!")

    return new_func


@decorator2
def decorated2():
    print("Hello!")


decorated2()
print(decorated2.__name__)

# Logging to file decorator
# *args is tuple and **kwargs is Keywords key=val
# decorated = decorator(decorated)

# In pseudocode
# simple_func = logger(simple_func)
import functools


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Decorator Example: In the wrapper: {result}")
        with open('logging_file.txt', 'a+') as f:
            f.write(f'{result}\n')
        return result

    return wrapped


@logger
def simple_func(list_num):
    print("This is Simple Func")
    return sum(list_num)


@logger
def another_simple_func(*args, **kwargs):
    for k, v in kwargs.items():
        print(f'{k}={v}')
    return kwargs


res = simple_func([1, 2, 3, 4, 5])
print(f'{res}')

another_simple_func(par1=23, par2=45)

# Using funtools.wraps(func) we can save the original function name
print(simple_func.__name__)


# Decorator with parameter - Double decorator

def logger2(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"Decorator Example: In the wrapper: {result}")
            with open(filename, 'a+') as f:
                f.write(f'{result}\n')
            return result

        return wrapped

    return decorator


@logger2('logging_file.txt')
def simple_func2(list_num):
    print("This is Simple Func2")
    return sum(list_num)


res = simple_func2([1, 2, 3, 4, 5, 6])
print(f'{res}')


def first_d(func):
    def wrapped():
        print("This is First Decorator")
        return func()

    return wrapped


def second_d(func):
    def wrapped():
        print("This is Second Decorator")
        return func()

    return wrapped


# In psuedocode
# test_function = first_decorator(second_decorator(test_function())
@first_d
@second_d
def test_function():
    print("This is test function")


test_function()
print('-------------------')


# Generators

def my_range(start, stop):
    cur = start
    while cur < stop:
        yield cur
        print(f"After returning cur {cur}")
        cur += 1


for i in my_range(1, 5):
    print(i)

my_gen = my_range(1, 5)
nxt = my_gen.__next__()
print(f'Generator\'s next {nxt}')

# same
nxt = next(my_gen)
print(f'Generator\'s next {nxt}')
print('-------------------')


# Impl Fibonacci ( 1,1,2,3,5,8,13,21,...) using generator

def fib(num):
    a = 1
    b = 1
    for i in range(1, num):
        yield a
        a, b = b, a + b


for f in fib(10):
    print(f'Fibonacci number {f}')
print('-------------------')

# Classes and Objects
num = 18
print(isinstance(num, int))


# class declaration

# class Human:
#     """This class defines a human"""
#     pass
#
#
# class Robot:
#     """This class defines a Robot"""
#
#
# print(Robot)
# print(Robot.__name__)

# We use one underscore "_" in class attributes to indicate that these are "hidden" attributes
# _say is a private method
class Human:
    """Ths class defines humans"""

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    # Static method does not take any arguments
    # It used in the centext of the class
    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

    def _say(self, text):
        print(text)

    def say_how_old(self):
        self._say(f"I and {self._age} years old")

    def say_name(self):
        self._say(f"My name is {self._name}")


class Planet:
    """The Class that defines planets"""

    # Class attribute
    count = 0

    # We redefining constructor __new__() which takes class Planet and initialization parameters ("Mars")
    def __new__(cls, *args, **kwargs):
        print(f"Planet __new__ called")
        object = super().__new__(cls)
        return object

    # Initializer __init__() is called aftr object has been created
    def __init__(self, name, population=None):
        print(f"Planet _init__ called")
        self.name = name
        self.population = population or []
        Planet.count += 1

    def add_human(self, human):
        print(f"Welcome to {self.name} {human._name}!")
        self.population.append(human)

    def __str__(self):
        return self.name


# # Not recommended - use dedicated methods
#     def __del__(self):
#         print(f"Calling planet destructor for {self.name} Goodbye!")

# represent class when object is printed
def __repr__(self):
    return f"Planet {self.name}"


planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranis", "Neptune"]
solar_system = []

for name in planet_names:
    solar_system.append(Planet(name))

print(solar_system)

print(f"Total number od planet {Planet.count}")

mars = Planet("Mars!")
# same resilt evem if we use object instead of Class
print(mars.name)
print(mars.count)
# del mars.name

print(mars.__dict__)
mars.weight = 6.39e23
print(mars.__dict__)
print(mars.__doc__)
print(mars.__class__)

# Class Attributes


# Destructor
# __del__

bob = Human(name="Bob", age="22")
bob.say_name()
bob.say_how_old()

print(Human.is_age_valid(22))

planet = Planet("Mars")
planet.add_human(bob)
print(planet.population)


class Robot:
    """This class define a robot"""

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        print(f"We are in power setter")
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print(f"Deleting imternal _power")
        del self._power


irobot = Robot(22)
irobot.power = 25

from datetime import date


def extract_description(user_input):
    return f"Fifa World Cup"


def extract_date(user_input):
    return date(2018, 6, 14)


class Event:
    """Class for smart helper"""

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event: {self.description} at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)


# Methods are the functions that act in the context of the class object
def main():
    pass


if __name__ == "__main__":
    main()
