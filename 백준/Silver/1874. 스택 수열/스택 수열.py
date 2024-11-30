import sys
input = sys.stdin.readline

n = int(input())
sequence = []

for _ in range(n):
  sequence.append(int(input()))
sequence.reverse()

stk = []
history = []
i = 1

while sequence:
  if stk and stk[-1] == sequence[-1]:
    stk.pop()
    sequence.pop()
    history.append('-')
  else:
    if i > n:
      break
    stk.append(i)
    history.append('+')
    i += 1

if stk:
  print('NO')
else:
  for c in history:
    print(c)