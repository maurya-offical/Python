print("1:Sum","2:Subtract","3:Multiply","4:Divide","5:Square","6:Cube")
print("Note:-In case of cube and square you have to place the value of b is zero")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
def add(a,b):
  return(a+b)
def sub(a,b):
  return(a-b)
def mul(a,b):
  return(a*b)
def division(a,b):
  return(a/b)
def square(a,b):
  return(a*a) 
def cube(a,b):
  return(a*a*a)
chioce=int(input("Enter your choice:"))
if chioce==1:
  print("The sum of a and b is",add(a,b))
elif chioce==2:
  print("The subtraction of a and b is",sub(a,b))
elif chioce==3:
  print("The multiplication of a and b is",mul(a,b))
elif chioce==4:
  print("The division of a and b is",division(a,b))
elif chioce==5:
  print("The square of a is",square(a,b))
elif chioce==6:
  print("The cube of a and b is",cube(a,b))
else:
  print("Invalid")