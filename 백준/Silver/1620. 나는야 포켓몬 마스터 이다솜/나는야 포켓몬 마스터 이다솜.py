import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for i in range(1, n + 1):
  poke = input().rstrip()
  dic[str(i)] = poke
  dic[poke] = i

for _ in range(m):
  question = input().rstrip()
  print(dic[question])