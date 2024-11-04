n, b = input().split()

trans_v = ord('A') - 10
sum = 0

for i, c in enumerate(n[::-1]):
  num = 0
  
  try:
    num = int(c) * (int(b) ** i)
  except ValueError:
    num = (ord(c) - trans_v) * (int(b) ** i)
  finally:
    sum += num

print(sum)