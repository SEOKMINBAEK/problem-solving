n = int(input())
nums = map(int, input().split())
min = 1000000
max = -1000000

for num in nums:
  if num < min:
    min = num
  if num > max:
    max = num

print(min, max)