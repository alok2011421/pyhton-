logo = """
 _____________________
|  _________________  |
| |              0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

while True:
    n1=int(input("Enter the First no :")) 
    op_per=input("Enter the operation you want to perform \n+\n-\n*\n/\n")
    n2=int(input("Enter the second no :"))
    #op_per=int(input("Select the operation you want to perform\n 1 for + \n 2 for - \n 3 for *\n 4 for /\n"))
    if op_per=="+":
        c=print(add(n1,n2))
    elif op_per=="-":
        c=print(sub(n1,n2))
    elif op_per=="*":
        c=print(mul(n1,n2))
    elif op_per=="/":
        c=print(div(n1,n2))
    else:
        print("Invalid selection")
    a=input("Do you want to continue with this result or want to start new calculation?").lower()
    if a=="yes":
        n1=c
    else:
        break