print("Enter your choice: 1-add,2-subtract,3-maultiply,4-divide,5-squre,6-cube")
print("Note:-In case of Square And Cube you have put the value of b is 0")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
def square(a):
    return (a*a)
def cube(a):
    return(a*a*a)
num=int(input("Enter your choice:"))

if num==1:
    print("The sum of a and b is:",add(a,b))
elif(num==2):
    print("The subtraction of a and b is:",subtract(a,b))
elif(num==3):
    print("The multiplication a and b is:",multiply(a,b))
elif(num==4):
    print("The division of a and b is:",divide(a,b))
elif(num==5):
    print("The square of a is:",square(a))
elif(num==6):
    print("The Cube of a is:",cube(a))
else:
    print("Invalid Input")
