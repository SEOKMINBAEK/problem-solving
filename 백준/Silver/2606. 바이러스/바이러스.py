n = int(input())
m = int(input())
graph = { str(i): [] for i in range(1, n + 1) }
visited = set()
cnt = 0

def dfs(s):
  global cnt
  visited.add(s)
  
  for node in graph[s]:
    if node not in visited:
      cnt += 1
      dfs(node)

for _ in range(m):
  s, t = input().split()
  graph[s].append(t)
  graph[t].append(s)

dfs('1')
print(cnt)