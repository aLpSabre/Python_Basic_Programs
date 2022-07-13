my_list=[11,12,13,14,15]
odd=0
evn=0
for i in my_list :
  if i%2==1:
    odd=odd+1
  else :
    evn=evn+1
print(f"The number of odd numbers :{odd}")
print(f"The number of even numbers :{evn}")