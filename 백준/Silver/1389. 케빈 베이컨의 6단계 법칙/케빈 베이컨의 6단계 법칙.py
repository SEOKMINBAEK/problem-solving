import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = { i: [] for i in range(1, n + 1) }
dic = {i: 0 for i in range(1, n + 1)}

for _ in range(m):
  a, b = map(int, input().split())
  
  if b not in graph[a]:
    graph[a].append(b)
  
  if a not in graph[b]:
    graph[b].append(a)

def bfs(node):
  queue = [(node, 0)]
  visited = [node]
  
  total = 0
  
  for cur in queue:
    total += cur[1]
    
    for n in graph[cur[0]]:
      if n not in visited:
        queue.append((n, cur[1] + 1))
        visited.append(n)
  
  dic[node] = total

for key in graph:
  bfs(key)

print(min(dic, key=dic.get))