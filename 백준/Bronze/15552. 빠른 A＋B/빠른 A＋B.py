import sys

t = int(input())

for i in range(0, t):
  nums = sys.stdin.readline().strip()
  a, b = map(int, nums.split())
  print(a + b)