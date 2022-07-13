def lengthOfLongestSubstring(s):
    myword=""
    lenght=0
    row=0
    if len(s)==1:
        return 1
    if len(set(s))==len(s) and list(set(s))!=list(s):
      return len(s)
    if len(set(s))==1:
      return 1   
    for i in range(len(s)):
        row=row+1
        
        for k in range(row,len(s)+1):
            if s[i]!= s[k-1]:

              try_word=s[i:k]
              print("tryword1",try_word)
              if len(set(try_word))!=len(try_word):
                break
              print(try_word,"tryword")
              if len(set(try_word))==len(try_word) and lenght<len(try_word):
                  myword=try_word
                  lenght=len(try_word)
                  print(myword,"myword",lenght,"length")
    return lenght


print(lengthOfLongestSubstring(s="wwwp"))    