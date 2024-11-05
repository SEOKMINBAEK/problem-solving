n = int(input())

i = 0
sum = 0
# 팩토리얼i = sum, sum이 n보다 크면 종료
while sum < n:
  i+=1
  sum += i

# 시작 행 or 열에서 움직여야할 수
jump = (i - (sum - n)) - 1

if i % 2: # 홀수면 i번 열에서 시작
  x, y = (i, 1)
  for _ in range(0, jump):
    x = x - 1
    y = y + 1
else: # 짝수면 i번 행에서 시작
  x, y = (1, i)
  for _ in range(0, jump):
    x = x + 1
    y = y - 1

print("%d/%d" % (x, y))
