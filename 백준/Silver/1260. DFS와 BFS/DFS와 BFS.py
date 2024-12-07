import sys
input = sys.stdin.readline

n, m ,v = map(int, input().split())
graph = { i + 1: [] for i in range(n) }
dfs_visited = set()
bfs_visited = set()

dfs_result = []
bfs_result = []

def dfs(s):
  dfs_visited.add(s)
  dfs_result.append(str(s))
  
  graph[s].sort()
  
  for node in graph[s]:
    if node not in dfs_visited:
      dfs(node)

def bfs(root):
  q = [root]
  
  while q:
    s = q.pop(0)
    if s in bfs_visited: continue
    
    bfs_visited.add(s)
    bfs_result.append(str(s))
    
    graph[s].sort()
    for node in graph[s]:
      q.append(node)

for _ in range(m):
  s, t = map(int, input().split())
  graph[s].append(t)
  graph[t].append(s)

dfs(v)
bfs(v)

print(' '.join(dfs_result))
print(' '.join(bfs_result))