import math
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
    determinant = b**2-4*a*c
    if (determinant<0):
        x1 = -b/(2*a)
        i1 = determinant/(2*a)
        x2 = -b/(2*a)
        i2 = -determinant/(2*a)
        print("The imaginary roots are", str(x1), "+ " + str(i1) +"i and", str(x1), "+", str(i2), "i")
    elif (determinant == 0):
        x = (-b)/(2*a)
        print("The one root is:", x)
    else:
        x1 = (-b+math.sqrt(determinant))/(2*a)
        x2 = (-b-math.sqrt(determinant))/(2*a)
        print("The two roots are", x1, "and", x2)
main()