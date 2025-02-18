import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 도시의 크기, M: 최대 치킨집의 개수
chickens = [] # 치킨집 좌표 배열
houses = [] # 집 좌표 배열
result = float('inf')

for i in range(N):
  for j, char in enumerate(input().rstrip().split()):
    if char == '2':
      chickens.append((i, j))
    if char == '1':
      houses.append((i, j))

result = float('inf')

for m_len_shop in combinations(chickens, M):
  total = 0
  
  for house in houses:
    mini = float('inf')
    for shop in m_len_shop:
      mini = min(mini, abs(house[0] - shop[0]) + abs(house[1] - shop[1]))
    
    total += mini
  
  result = min(result, total)

print(result)