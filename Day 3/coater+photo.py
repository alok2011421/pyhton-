print("Welcome to the rollarcoater")
h=int(input("Enter the height in cm: "))
c=0
if h>120:
    print("You are eligible to ride")
    a=int(input("Enter Your age"))
    if a<=12:
        c=5
    elif a>12 and a<=18:
        c=7
    else:
        c=12
    p=input("Do you want photo?")
    if p == "Y":
        c+=5
    print(c)
else:
    print("You are not eligible to ride")
