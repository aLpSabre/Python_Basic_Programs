word="hippo runs to us!"
mydict=dict()
count=0
for i in word:
  if i in mydict:
    mydict[i]=mydict[i]+1
  else:
    mydict[i]=1
print(mydict)