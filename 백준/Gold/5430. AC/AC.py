import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  commands = input().rstrip()
  _ = int(input())
  arr = deque(eval(input().rstrip()))
  
  is_reverse = False
  is_error = False
  
  for i, cmd in enumerate(commands):
    if cmd == 'R':
      is_reverse = not is_reverse
    else:
      if len(arr):
        if is_reverse:
          arr.pop()
        else:
          arr.popleft()
      else:
        is_error = True
        break
  
  if is_error:
    print('error')
  else:
    if is_reverse:
      arr.reverse()
    print(f"[{','.join(str(x) for x in arr)}]")