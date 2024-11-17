import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  ps = input().rstrip()
  stk = []
  is_pare = True
  
  if ps[0] != '(':
    is_pare = False
  else:
    for c in ps:
      if c == '(':
        stk.append(c)
      else:
        if len(stk) < 1: # 스택이 비었는데 )이 등장하면
          is_pare = False
          break
        else:
          stk.pop()
    
  if is_pare and len(stk) == 0:
    print("YES")
  else:
    print("NO")