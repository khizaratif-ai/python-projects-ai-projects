try:
    width = float(input("enter width: "))
    length = float(input("enter length: "))

    if width == length:
        exit("That looks like a square!!")

    area = width * length
    print("the area is:", area)
except ValueError:
    print("\n" + "Enter a number!!")