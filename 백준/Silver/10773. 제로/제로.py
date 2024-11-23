import sys
input = sys.stdin.readline

n = int(input())
stk = [0]

for _ in range(n):
  v = int(input())
  
  if v == 0:
    stk.pop()
  else:
    stk.append(v)

print(sum(stk))