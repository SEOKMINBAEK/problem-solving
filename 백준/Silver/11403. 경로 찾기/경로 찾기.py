import sys
input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

for k in range(n): # 거쳐가는 노드
  for i in range(n): # 출발하는 노드
    for j in range(n): # 도착하는 노드
      if graph[i][k] and graph[k][j]: # i -> k 가 연결되 있고 k -> j가 연결되있으면 i -> j 로 가는 길이 존재
        graph[i][j] = 1

for row in graph:
  print(' '.join(str(x) for x in row))