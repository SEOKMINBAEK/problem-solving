n, m = map(int, input().split())

mtx = [[] for _ in range(n)]

for i in range(n):
  for c in input():
    mtx[i].append(int(c))

queue = [ { 'offset': (0, 0), 'distance': 1 } ]
visited = set()

for cur in queue:
  if cur['offset'] in visited:
    continue
  else:
    visited.add(cur['offset'])
  
  if cur['offset'][0] < 0 or cur['offset'][0] >= n or cur['offset'][1] < 0 or cur['offset'][1] >= m:
    continue
  
  if cur['offset'] == (n - 1, m - 1):
    print(cur['distance'])
    break
  
  if cur['offset'][0] + 1 < n and mtx[cur['offset'][0] + 1][cur['offset'][1]] != 0:
    queue.append({ 'offset': (cur['offset'][0] + 1, cur['offset'][1]), 'distance': cur['distance'] + 1 })
  
  if cur['offset'][0] - 1 > -1 and mtx[cur['offset'][0] - 1][cur['offset'][1]] != 0:
    queue.append({ 'offset': (cur['offset'][0] - 1, cur['offset'][1]), 'distance': cur['distance'] + 1 })
  
  if cur['offset'][1] + 1 < m and mtx[cur['offset'][0]][cur['offset'][1] + 1] != 0:
    queue.append({ 'offset': (cur['offset'][0], cur['offset'][1] + 1), 'distance': cur['distance'] + 1 })
  
  if cur['offset'][1] + 1 > -1 and mtx[cur['offset'][0]][cur['offset'][1] - 1] != 0:
    queue.append({ 'offset': (cur['offset'][0], cur['offset'][1] - 1), 'distance': cur['distance'] + 1 })