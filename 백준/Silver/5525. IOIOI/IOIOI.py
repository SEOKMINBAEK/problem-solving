import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

i = 0
cnt = 0 # P(n)이 발견
oi_cnt = 0 # OI가 연속된 횟수

while i < M - 1:
  if S[i:i + 3] == 'IOI': # IOI 패턴이 발견되면
    oi_cnt += 1 # P(1)로써 카운트 시작
    i += 2 # 2칸 점프
    
    if oi_cnt == N: # P(n)이 완성된경우
      cnt += 1 # 카운트
      oi_cnt -= 1 # 좌측 OI 제거
  else:
    oi_cnt = 0 # 패턴이 끊기면 OI카운트 초기화
    i += 1

print(cnt)