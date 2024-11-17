import sys
input = sys.stdin.readline

q = []
n = int(input())

for _ in range(n):
  command = input().split()
  
  if command[0] == "push":
    q.append(command[1])
  elif command[0] == "pop":
    if len(q) == 0:
      print(-1)
    else:
      print(q.pop(0))
  elif command[0] == "size":
    print(len(q))
  elif command[0] == "empty":
    print(0 if len(q) else 1)
  elif command[0] == "front":
    if len(q) == 0:
      print(-1)
    else:
      print(q[0])
  elif command[0] == "back":
    if len(q) == 0:
      print(-1)
    else:
      print(q[-1])