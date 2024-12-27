import sys
input = sys.stdin.readline

n, k = map(int, input().split())
units = [0] * n

for i in range(n - 1, -1, -1):
  units[i] = int(input())
cnt = 0

for unit in units:
  cnt += k // unit
  k = k % unit

print(cnt)