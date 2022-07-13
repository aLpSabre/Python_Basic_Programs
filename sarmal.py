mylist = [
[ 13, 14, 15, 16, 1],
[ 12, 23, 24, 17, 2],
[ 11, 22 ,25, 18, 3],
[ 10, 21, 20, 19, 4],
[   9,   8,   7,   6,  5]
]
sorted=[]
length=len(mylist)
k=0
check=0
last=0

while check<2:
  
  for i in range(0+k,length-k):
    sorted.append(mylist[i][4-k])
    
  for i in range(1+k,length-k):
  
    sorted.append(mylist[4-k][length-i-1])


  for i in range(1+k,length-k):

    sorted.append(mylist[length-i-1][0+k])


  for i in range(1+k,length-1-k):
    sorted.append(mylist[0+k][i-length])
    if i==length-2-k:
      k=k+1
      check=check+1
      if check==2:
        for i in range(0+k,length-k):
          sorted.append(mylist[i][4-k]) 
    
print(sorted)