import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []

for _ in range(k):
  lines.append(int(input()))

start = 1
end = max(lines)
div = 0

while start <= end:
  mid = (start + end) // 2
  cnt = sum(line // mid for line in lines)
  
  if cnt >= n:
    div = mid
    start = mid + 1
  else:
    end = mid - 1

print(div)