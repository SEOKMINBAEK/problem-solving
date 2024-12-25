"""
도착점에서 n-1번째 계단을 밟고 오는 경우
dp[n] = dp[n-3] + steps[n-1] + steps[n]

도착점에서 n-2번째 계단을 밟고 오는 경우
dp[n] = dp[n-2] + steps[n]
"""

n = int(input())
steps = [0] * (n + 1)

for i in range(1, n + 1):
  steps[i] = int(input())

dp = [0] * (n + 1)

dp[1] = steps[1]
if n >= 2:
  dp[2] = steps[1] + steps[2]
if n >= 3:
  dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])

for i in range(4, n + 1):
  dp[i] = max(dp[i - 3] + steps[i - 1] + steps[i], dp[i - 2] + steps[i])

print(dp[i])