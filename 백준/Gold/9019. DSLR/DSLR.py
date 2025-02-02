import sys
from collections import deque
input = sys.stdin.readline

def D(n):
  return n * 2 % 10000

def S(n):
  return n - 1 if n > 0 else 9999

def L(n):
  n = str(n)
  n = ('0' * (4 - len(n))) + n
  n = n[1:] + n[0]
  return int(n)

def R(n):
  n = str(n)
  n = ('0' * (4 - len(n))) + n
  n = n[3] + n[:3]
  return int(n)

T = int(input())

for _ in range(T):
  A, B = map(int, input().split())
  
  queue = deque([(A, '')])
  visited = set()
  
  while queue:
    num, cmd = queue.popleft()
    
    if num == B:
      print(cmd)
      break
    
    d = D(num)
    s = S(num)
    l = L(num)
    r = R(num)
    
    if d not in visited:
      queue.append((d, cmd + 'D'))
      visited.add(d)
    
    if s not in visited:
      queue.append((s, cmd + 'S'))
      visited.add(s)
    
    if l not in visited:
      queue.append((l, cmd + 'L'))
      visited.add(l)
    
    if r not in visited:
      queue.append((r, cmd + 'R'))
      visited.add(r)