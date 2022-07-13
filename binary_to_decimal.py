bin=input("Pls enter a bin number :")
decimal=0
for i in reversed(range(0,len(bin))):
  decimal=decimal+(2**(len(bin)-i-1))*(int(bin[i]))
  
print("Decimal number is ",decimal)