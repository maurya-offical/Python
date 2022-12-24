'''#line Graph
import matplotlib.pyplot as plt
a=[1,2,3,4]
b=[2,4,6,8]
plt.plot(a,'r',b,)
plt.title("Shivam")
plt.xlabel("Bikes")
plt.ylabel("Cost")
plt.show()'''

#bar graph
'''import matplotlib.pyplot as plt
a=[2,4,6,8]
b=[4,6,8,10]
plt.bar(a,b,)
plt.title("Shivam")
plt.xlabel("Bikes")
plt.ylabel("Cost")
plt.show()'''

#histogram
'''import matplotlib.pyplot as plt
a=[2,4,6,8]
b=[4,6,8,10]
plt.hist(a,b,)
plt.title("Shivam")
plt.xlabel("Bikes")
plt.ylabel("Cost")
plt.show()

#many values in multiple varriabes

x,y,z="Shivam","Rivesh","Ashish"
print(x,y,z)'''


'''def str_count(a):
    for i in range(len(a)):
        print(a[i])
        i=i+1
str_count("Shivam")'''

'''def str_count(a):
    for i in range(len(a)):
        print(a[:i])
        i=i+1
str_count("Shivam")'''

'''a=5
b=6
c=a+b
print(c)'''


'''a = input("Enter The Value Of a:")
b = input("Enter the valur of b:")

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")'''

'''dict={"Rivesh":18,"Shivam":19}
print(dict)'''

'''num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
fac = fac * i
i = i + 1
 
print("factorial of ", num, " is ", fac)'''

'''num = int(input("enter a number: "))
fac = 1
i = 1
while i <= num:
 fac = fac * i
i = i + 1
print("factorial of ", num, " is ", fac)'''

'''a=int(input("Enter the number:"))
b=a
reverse=0
while(a>0):
  c=a%10
  reverse=reverse*10+c
  a=a//10
if(b==reverse):
  print("the number is palindrome")
else:
  print("Not a palindrome")'''

a=input("Enter the string:")
def palindrome():
  i=0
  j=len(a)-1
  while i<=len(a)-1 & j>=0:

    if(a[i] != a[j]):
      return False
    else:
       i=i+1
       j=j-1
       return True
palindrome(a)
