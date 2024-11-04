n, m = map(int, input().split())

a = [] 
b = []

for _ in range(0, n):
  a.append(list(map(int, input().split())))

for _ in range(0, n):
  b.append(list(map(int, input().split())))

for i in range(0, n):
  temp = []
  for j in range(0, m):
    temp.append(str(a[i][j] + b[i][j]))
  
  print(" ".join(temp))