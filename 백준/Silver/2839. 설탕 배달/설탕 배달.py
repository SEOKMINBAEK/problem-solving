n = int(input())
i = 0

while n >= 3:
  q, r = divmod(n, 5)
  
  if r == 0:
    n = 0
    i += q
    break
  else:
    n -= 3
    i += 1

if n == 0:
  print(i)
else:
  print(-1)