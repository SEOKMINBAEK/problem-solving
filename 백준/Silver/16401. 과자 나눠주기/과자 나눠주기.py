import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

l, r = 1, max(snacks)
result = 0

while l <= r:
  mid = (l + r) // 2
  cnt = sum(list((map(lambda x: x // mid, snacks)))) # 현재 값으로 과자를 나눈 몫만 합산
  
  if cnt >= M: # 현재 길이로 M명 이상에게 나눠줄 수 있으면
    result = mid
    l = mid + 1
  else: # 현재 길이로 M명 이상에게 나눠줄 수 없으면
    r = mid - 1

print(result)