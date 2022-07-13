def missing_char(word, n):
    if n < len(word):
        new=""
        for i in word:
            if word.index(i)!=n: 
                new=new+i
    return new
print(missing_char('kitchen', 0))