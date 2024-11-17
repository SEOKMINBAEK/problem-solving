import sys
input = sys.stdin.readline

n = int(input())
cards = input().split()
dic = {}

for card in cards:
  if dic.get(card):
    dic[card] += 1
  else:
    dic[card] = 1

m = int(input())
nums = input().split()

result = []
for num in nums:
  if dic.get(num):
    result.append(str(dic[num]))
  else:
    result.append('0')

print(" ".join(result))