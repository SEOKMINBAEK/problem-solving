word = input()

croa = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")

cnt = 0

while len(word) > 0:
  c = word[0]
  if c in ('c', 'd', 'l', 'n', 's', 'z'):
    if word[:2] in croa:
      word = word[2:]
    elif word[:3] in croa:
      word = word[3:]
    else:
      word = word[1:]
  else:
    word = word[1:]
    
  cnt += 1

print(cnt)