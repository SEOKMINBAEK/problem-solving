n, m = map(int, input().split())

maxi = 0
mini = 0

bigger = max(n, m)
smaller = min(n, m)

for i in range(smaller, 0, -1):
  if n % i == 0 and m % i == 0:
    maxi = i
    break

for i in range(1, smaller + 1):
  if (bigger * i) % smaller == 0:
    mini = bigger * i
    break

print(maxi)
print(mini)