n = int(input())
res = 0

for i in range(0, n):
  sum = 0
  for j in str(i):
    sum += int(j)
  
  if i == (n - sum):
    res = i
    break

print(res)