num=input("Pls enter a number: ")

for i in num:
  if(num[0]!=i and num.isdigit() and len(num)==4):  # To only get the numbers with 4 digits
    break                                           # and check if the at least two numbers are different

else:
  print("Pls enter a valid number")
  num=input("Pls enter a number: ")

user_input=num

def smallToBig(n):  # to put the number in order from small to
  nums=list(n)
  nums.sort()
  return nums

def arrayToString(x):   # to change list to string 
  num=""
  for i in x:
    num=num+i
  return num



count=0   # to count number of operations 

for i in range(0,7):    # to itarate over only 7 times 
  num1=int(arrayToString(smallToBig(num)))
  num2=int(arrayToString(smallToBig(num))[::-1])  # to reverse number from big to small
  num3=num2-num1  # to get the result

  count=count+1   # increment it one more at every operation
  
  if(num3!=6174):   # to check if the number not equal to 6174
   num=str(num3)
  else:
    break

print(f"The number {user_input} has reached to the 6174 at the count of {count}")