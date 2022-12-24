#Sum of the natural numbers.
#creating function
def natural_sum():
  #user imput
  num=int(input("Enter the number:"))
  sum=0
  #itration
  for i in range(1,num+1):
    print(i,end=" ")
    sum=sum+i
  #printing
  print("Sum is:",sum)
#calling the function
natural_sum()