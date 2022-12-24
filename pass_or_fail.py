print("Enter the marks of 5 subjects of a student:")
a=int(input("Enter the marks of 1st subject:"))
b=int(input("Enter the marks of 2st subject:"))
c=int(input("Enter the marks of 3rd subject:"))
d=int(input("Enter the marks of 4th subject:"))
e=int(input("Enter the marks of 5th subject:"))
sum=a+b+c+d+e
print(sum)

percent=sum/5
print("Percentage",percent)

if (percent>=33):
    print("Congrats you are Passed")
else:
    print("Sorry you are Fail")