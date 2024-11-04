n, b = map(int, input().split())
result = ""

while True:
  q, r = divmod(n, b)
  
  if r > 9:
    r = chr(r + 55)
  result += str(r)
  
  n = q
  if n == 0:
    break

print(result[::-1])