n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b, reverse=True)

total = 0

for i in range(n):
  total += sorted_a[i] * sorted_b[i]

print(total)