print("Welcome to Rollarcoaster")
h=int(input("Enter the height in cm: "))
if h>=120:
    a=int(input("Enter the age: "))
    c=0
    if a<=18:
        c=7
    else:
        c=10
    print(c)
else:
    print("You are not Eligible")