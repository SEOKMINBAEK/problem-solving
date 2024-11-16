import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  arr.append(tuple(input().rstrip().split()))

arr.sort(key=lambda v: (int(v[0]), int(v[1])))

for v in arr:
  print(v[0], v[1])