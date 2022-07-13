strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
ang={}

for item in strs :
  element="".join(sorted(item))
  if element  in ang :
    ang[element].append(item)
  else:
    ang[element]=[item]
print(ang)
print(list(ang.values()))