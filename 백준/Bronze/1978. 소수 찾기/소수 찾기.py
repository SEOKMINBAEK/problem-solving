n = int(input())
nums = list(map(int, input().split()))

for num in nums:
  if num < 2:
    n -= 1
    continue
  
  for i in range(2, num):
    if num % i == 0:
      n -= 1
      break

print(n)