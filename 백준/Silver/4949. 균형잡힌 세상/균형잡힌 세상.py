import sys
input = sys.stdin.readline

while True:
  str = input().rstrip()
  if str == '.':
    break
  
  stk = []
  is_pare = True
  
  for c in str:
    if c == '(':
      stk.append(c)
    elif c == '[':
      stk.append(c)
    elif c == ')':
      if len(stk) == 0 or stk[-1] != '(':
        is_pare = False
        break
      else:
        stk.pop()
    elif c == ']':
      if len(stk) == 0 or stk[-1] != '[':
        is_pare = False
        break
      else:
        stk.pop()
  
  if is_pare:
    print("yes" if len(stk) == 0 else 'no')
  else:
    print('no')