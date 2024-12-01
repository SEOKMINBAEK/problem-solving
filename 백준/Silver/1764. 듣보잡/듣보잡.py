import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for _ in range(n):
  dic[input().rstrip()] = False

for _ in range(m):
  unlook = input().rstrip()
  if dic.get(unlook) is not None:
    dic[unlook] = True

filtered = [key for key, value in dic.items() if value]
filtered.sort()

print(len(filtered))
print('\n'.join(filtered))