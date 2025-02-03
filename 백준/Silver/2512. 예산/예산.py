N = int(input()) # 지방의 수
locals = list(map(int, input().split()))
M = int(input()) # 총 예산

l, r = 0, max(locals)

while l <= r:
  mid = (l + r) // 2
  tot = sum(min(mid, x) for x in locals) # 상한액 기준으로 배정할 예산의 합
  
  if tot > M: # 배정할 예산의 합이 총 예산을 초과하는 경우
    r = mid - 1
  else: # 초과되지 않는 경우
    l = mid + 1

print(r)