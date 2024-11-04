t = int(input())
unit = [25, 10, 5, 1]

for _ in range(0, t):
  c = int(input())
  result = []
  
  for i in range(0, 4):
    q, r = divmod(c, unit[i])
    result.append(str(q))
    c = r
  
  print(" ".join(result))