import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for _ in range(n):
  cmd = input().rstrip().split()
  dic[cmd[0]] = cmd[1]

for _ in range(m):
  print(dic[input().rstrip()])