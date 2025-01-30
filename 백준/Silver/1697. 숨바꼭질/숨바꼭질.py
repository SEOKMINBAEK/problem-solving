n, k = map(int, input().split())

graph = [0 for _ in range(100001)]

queue = [n]
visited = { n }

for cur in queue:
  if cur == k:
    print(graph[cur])
    break
  
  if cur - 1 not in visited and cur - 1 > -1:
    graph[cur - 1] = graph[cur] + 1
    queue.append(cur - 1)
    visited.add(cur - 1)
  
  if cur + 1 not in visited and cur + 1 < 100001:
    graph[cur + 1] = graph[cur] + 1
    queue.append(cur + 1)
    visited.add(cur + 1)
  
  if cur * 2 not in visited and cur * 2 < 100001:
    graph[cur * 2] = graph[cur] + 1
    queue.append(cur * 2)
    visited.add(cur * 2)