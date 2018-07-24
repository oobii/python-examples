def main():
    # This is a comment
    #
    # snake_case = "Python"
    for i in range(4):
        print(i)

    # Access to inline documentation
    # >>> print.__doc__

    """
    Multi line
    comments
    """

    def myfunc():
        print("My function")

    3 ** 2
    10 // 3
    10 % 3

    x1, y1 = 1, 3

    x1, y1 = y1, x1

    x = y = 0
    # different from
    lx = ly = []
    lx.append(11)
    lx.append(22)
    print("List is a Chanegable object {} {}".format(lx, ly))

    num = 150.2
    print(num, type(num), int(num), type(int(num)))

    my_comp = 15 + 3j
    print(my_comp, type(my_comp), "real {} imag {}".format(my_comp.real, my_comp.imag))

    print(1 < x1 <= 4)

    x = 2
    y = False
    print(x or y)

    x = 2
    y = "boom"
    print(x and y)

    import calendar
    print(calendar.isleap(2000))
    my_sting = 'This ia test from "Coursera"'
    raw_example = r"file on disk c:\\"

    # place  holder with a name
    print("{raw} . It's address in memory {addr}".format(raw=raw_example, addr=id(raw_example)))

    # f-string
    z = 2 / 3
    print(f"X1 is equal {x1} and Y1 is equal {y1} and with Modificator {z:.3f}")

    # byte string
    greetings = "привет"
    encoded_str = greetings.encode(encoding="utf-8")
    for b in encoded_str:
        print(f"{b: #x}")

    decoded_str = encoded_str.decode(encoding="utf-8")
    print(f"\n{decoded_str}")

    answer = None
    print(type(None))

    income = None
    # idiomatic way to check object
    if income is None:
        print("Did not start yet ")
    elif not income:
        print("Income is zero")

    score = 5
    winner = "Argentina" if score > 0 else "Jamaica"

    for letter in winner:
        print(letter)

    for i in range(10,5,-1):
        print(i)

# Operator "pass"
# empty block
    for i in range(10,5,-1):
        pass

# in Python all is object
num = 2
print(dir(num))





if __name__ == "__main__":
    main()
