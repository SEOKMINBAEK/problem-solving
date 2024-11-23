n = int(input())
f = 1

for i in range(2, n + 1):
  f *= i

f = str(f)[::-1]

zero_cnt = 0
for c in f:
  if c == '0':
    zero_cnt += 1
  else:
    break

print(zero_cnt)