n, m = map(int, input().split())
basket = ['0'] * n

for _ in range(0, m):
  i, j, k = map(int, input().split())
  for idx in range(i - 1, j):
    basket[idx] = str(k)

print(" ".join(basket))