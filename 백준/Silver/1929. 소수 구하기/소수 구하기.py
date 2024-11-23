import math

m, n = map(int, input().split())
if m == 1:
  m = m + 1

nums = [v for v in range(m, n + 1)]

maxi = int(math.sqrt(n))
cnt = 2

while cnt <= maxi:
  nums = list(filter(lambda v: v == cnt or v % cnt, nums))
  cnt += 1

for v in nums:
  print(v)