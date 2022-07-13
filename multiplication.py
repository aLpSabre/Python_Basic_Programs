while True:
  entry=(input("Enter a number pls! "))
  if entry.isdigit() and 1<=int(entry)<=10:
    num=int(entry)
    break
  else :
    print("Pls enter only number between 1-10")
for i in range (1,11):
  print(f"{num} x {i}={num*i}")