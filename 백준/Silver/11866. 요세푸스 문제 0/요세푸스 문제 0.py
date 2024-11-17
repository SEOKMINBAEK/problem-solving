n, k = map(int, input().split())

q = [str(i) for i in range(1, n + 1)]
arr = []

while len(q):
  i = (k - 1) % len(q)
  arr.append(q.pop(i))
  l = q[:i]
  r = q[i:]
  q = r + l

print('<', end='')
print(", ".join(arr), end='')
print('>')