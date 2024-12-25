import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = nums[0]

for i in range(2, n + 1):
  dp[i] = nums[i - 1] + dp[i - 1]

for _ in range(m):
  i, j = map(int, input().split())
  
  print(dp[j] - dp[i - 1])