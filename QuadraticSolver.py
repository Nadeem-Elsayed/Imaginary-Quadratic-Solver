def main():
    print("A Quadratic Formula can be characterized by a formula such as:")
    print("y = ax^2 + bx + c")
    a = None
    b = None
    c = None
    while (a == None or isinstance(a, str)):
        try:
            a = float(input("Enter a proper double value for 'a' ex 5.6: "))
        except ValueError:
            continue
    while (b == None or isinstance(b, str)):
        try:
            b = float(input("Enter a proper double value for 'b' ex 5.6: "))
        except ValueError:
            continue
    while (c == None or isinstance(c, str)):
        try:
            c = float(input("Enter a proper double value for 'c' ex 5.6: "))
        except ValueError:
            continue
main()