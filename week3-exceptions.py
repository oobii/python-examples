# Exception Errors

# !!! Not all Exceptions classes have errno and strerror attributes

# obj = MyClass()
# obj.foo
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'MyClass' object has no attribute 'foo'
# d = {"foo": 1}
# d["bar"]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: 'bar'
# l = [1,2]
# l[3]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# IndexError: list index out of range
# int("aa")
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'aa'
# a+"aa"
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'a' is not defined
# l[0]+"aa"
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# we dont hadle this error
#     assert 1 == 0, "Something not equal"
# AssertionError: Something not equal


# while True:
#     try:
#         raw = input("Input number: ")
#         num = int(raw)
#     except ValueError as e:
#         print(f"Exception: {e}")
#     except KeyboardInterrupt:
#         print("Got Ctl-C")
#     else:
#         print("No Exceptions")
#         break

# while True:
#     try:
#         raw = input("Input number: ")
#         num = int(raw)
#     except ValueError as e:
#         print(f"Exception: {e}")
#     except KeyboardInterrupt:
#         print("Got Ctl-C")

# while True:
#     try:
#         raw = input("Input number: ")
#         num = int(raw)
#         total_count = 1000 / num
#         break
#     except (ValueError, ZeroDivisionError):
#         print("Wrong value")


# using parent exception
database = {
    "red": ["111","333"],
    "blue": ["aaa","bbb"]
}
try:
    val = database["red"][10]
    print(f"{val}")
except LookupError as e:
    print(f"error {e} - one of two types: KeyError or IndexError!")


try:
    val = database["redish"][0]
    print(f"{val}")
except LookupError as e:
    print(f"error {e} - one of two types: KeyError or IndexError!")

# f = open('testfile.txt')
# try:
#     for line in f:
#         # strip trailing whitespaced or listed chars
#         print(line.rstrip('\n'))
#         1/0
#     f.close()
# except OSError as e:
#     print(f"file error {e.errno} {e.strerror}")
# finally:
#     print(f"Still Closing our file: {f.name}")
#     f.close()

import os.path
filename = "/no/file"
try:
    if not os.path.exists(filename):
        raise ValueError("no such file", filename)
        f = open(filename)
except ValueError as err:
    msg, filename = err.args[0],err.args[1]
    print(f"Error  with this parameters: {msg} {filename}")

# import traceback
#
# try:
#
#     try:
#         1/0
#     except Exception:
#         trace = traceback.print_exc()
#         print(trace)
#         print("Our line here")
#         # to pass the exception up to the code
#         raise
#
# except Exception as e:
#     print(f"Outmost try block caught this")

# try:
#     1/0
# except ZeroDivisionError as err:
#     print(f"Zero error! {err}")
#
#     raise TypeError("Re-raising error") from err

# -O canturn off all assetr error checks
# assert 1 == 0, "Something not equal"

# Exception take long - lower the script performance

