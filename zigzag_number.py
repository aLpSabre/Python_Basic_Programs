def convert(s,numRows):
    if len(s)==1 or len(s)==2 or numRows==1:
        return s
    myword=""
    mylist=[]
    for i in range(numRows):
        mylist.append([])
      
    length=0
    row=0;
    while length<=len(s)-1:
        for i in range(row,numRows+row):
          if length==len(s):
            break;
          mylist[i-row].append(s[i])
          length+=1

        for i in (range(numRows+row,numRows+(numRows-2)+row)):
          if length==len(s) :
            break;
          mylist[(row+(numRows-2))-i].append(s[i])
          length+=1

        row=row+(numRows+(numRows-2))
        
    myword="".join(rows for row in mylist for rows in row)
    return (myword)
    
print(convert("abcdefg",3))