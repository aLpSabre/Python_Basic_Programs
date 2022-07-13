n=100
primes=list(range(2,n))

for i in range(2,n):
  for k in range (2,10):
    if i%k==0 and k!=i:
      primes.remove(i)
      break
       
print(primes)

"""
1. Another way of finding the list of prime numers in a choosen range

primes=[]

for k in range(2,100):
  for i in range(2,k):
      if (k % i) == 0:
          break
  else:
      primes.append(k)
       
print(primes)


2. Find if a number is a prime number 

num=input("Pls enter a number :")
check=False

if(int(num)>1):
  for i in range (2,int(num)):
    if int(num)%i==0:
      check=True
      break

if check:
  print(num," is a not prime number")
else:
  print(num," is a prime number")

"""
