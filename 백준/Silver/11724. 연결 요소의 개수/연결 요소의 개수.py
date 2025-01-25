import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
visited = set()

def dfs(node):
  if node in visited:
    return 0
  
  visited.add(node)
  
  for trg in graph[node]:
    dfs(trg)
  
  return 1

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

cnt = 0

for key in graph:
  cnt += dfs(key)

print(cnt)