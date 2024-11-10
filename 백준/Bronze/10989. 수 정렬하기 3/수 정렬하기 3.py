import sys

n = int(sys.stdin.readline())
num_li = [0 for i in range(0, 10001)]

for _ in range(0, n):
  num_li[int(sys.stdin.readline())] += 1

for i, v in enumerate(num_li):
  if v == 0: continue
  for _ in range(0, v):
    print(i)