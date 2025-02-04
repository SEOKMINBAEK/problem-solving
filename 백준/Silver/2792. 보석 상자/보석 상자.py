import sys
input = sys.stdin.readline

N, M = map(int, input().split())
gems = [0] * M

for i in range(M):
  gems[i] = int(input())

l, r = 0, max(gems)

while l <= r:
  jealous = (l + r) // 2
  cnt = 0
  
  if jealous == 0:
    l = 1
    break
  
  for gem in gems:
    cnt += (gem // jealous) + (1 if gem % jealous else 0)
  if cnt > N: # 나눠줄 수 있는 정원이 학생의 수 보다 큰 경우
    l = jealous + 1
  else: # 나눠줄 수 있는 정원이 학생의 수보다 작거나 같은 경우
    r = jealous - 1

print(l)