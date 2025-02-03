import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

l, r = 0, max(heights)

# 시작 포인터가 끝 포인터를 넘지 않을 때까지
while l <= r:
  mid = (l + r) // 2 # 절단기 높이를 탐색 바운더리의 중간으로 설정
  cut = sum(max(0, tree - mid) for tree in heights) # 잘라진 나무길이 합산(음수가 나오면 0으로 치환)
  
  if cut < M: # 길이가 모자란 경우 절단기 높이를 내린다
    r = mid - 1
  else: # 길이가 남거나 딱 맞는 경우 경우 절단기 높이를 올린다
    l = mid + 1 

print(r)