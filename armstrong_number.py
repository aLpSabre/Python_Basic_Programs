while True:
  num=input("Pls enter a number :")
  sum=0
  if num.isdigit():
    for i in range(0,len(num)):
      sum=sum+int(num[i])**len(num)
    if (sum==int(num)):
      print(f"{num} is an Armstrong number")
      break
    else:
      print(f"{num} is not an Armstrong number")
      break
  else :
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")