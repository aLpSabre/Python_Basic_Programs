
word="ab"
wordfirst=word[0]
wordlast=word[len(word)-1]
mylist=list(word)
mylist[0]=wordlast
mylist[len(word)-1]=wordfirst
newword=""
for i in mylist:
  newword+=i
print(newword)

"""
def change_string(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_string('a'))
print(change_string('12345'))
print('abcd'[1:-1])

"""