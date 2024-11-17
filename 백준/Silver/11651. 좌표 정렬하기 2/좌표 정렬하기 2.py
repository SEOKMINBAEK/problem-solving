import sys
input = sys.stdin.readline

offsets = []
n = int(input())

for _ in range(n):
  offsets.append(tuple(input().split()))

offsets.sort(key=lambda offset: (int(offset[1]), int(offset[0])))

for (x, y) in offsets:
  print(x, y)