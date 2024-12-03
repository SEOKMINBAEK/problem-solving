import sys
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n, 0, -1):
  q.append(i)

while len(q):
  print(q.pop())
  if len(q):
    q.insert(0, q.pop())