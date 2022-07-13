n=5
max=float('-inf')
mylist=[-7,-7,-7,-7,-6]

for i in range(0,n):
    check=mylist[i]
    if check>max:
        max=check
          
runner=0
checklist=[]
for i in mylist:
    if max!=i:
      checklist.append(i)

max=float('-inf')
for i in checklist:
    check=i
    if check>max:
        max=check
print(max)

# Second and easy way 
#  mylist=[-7,-7,-7,-7,-6]
#  x=list(set(mylist))
#  x.sort()
#  print(x[-2])
