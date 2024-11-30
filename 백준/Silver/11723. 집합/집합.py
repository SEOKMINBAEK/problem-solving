import sys
input = sys.stdin.readline

m = int(input())
s = set()
all_s = {str(i) for i in range(1, 21)}

for _ in range(m):
  command = input().rstrip().split()
  
  if command[0] == 'add':
    s.add(command[1])
  elif command[0] == 'remove':
    s.discard(command[1])
  elif command[0] == 'check':
    print(1 if command[1] in s else 0)
  elif command[0] == 'toggle':
    if command[1] in s:
      s.remove(command[1])
    else:
      s.add(command[1])
  elif command[0] == 'all':
    s = set(all_s)
  elif command[0] == 'empty':
    s = set()