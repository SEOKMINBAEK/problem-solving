import sys
input = sys.stdin.readline

N = int(input())
meets = [[0, 0] for _ in range(N)] # 시작시간, 종료시간

for i in range(N):
  meets[i][0], meets[i][1] = map(int, input().split())

meets.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for start, end in meets:
  if start >= end_time:
    cnt += 1
    end_time = end

print(cnt)