N, r, c = map(int, input().split())
length = 2 ** N

val = 0

def recursion(n, x, y):
  global val
  
  if n == 1:
    for row in range(x[0], x[1]):
      for col in range(y[0], y[1]):
        if row == r and col == c:
          print(val)
          exit(0)
        val += 1
    
    return
  
  if r < (x[0] + x[1]) // 2:
    if c < (y[0] + y[1]) // 2: # 제 2분면 안에 들어오는 경우
      val += 0
      recursion(n - 1, (x[0], (x[1] + x[0]) // 2), (y[0], (y[1] + y[0]) // 2))
    else: # 제 1분면 안에 들어오는 경우
      val += ((2 ** (n - 1)) ** 2) * 1
      recursion(n - 1, (x[0], (x[1] + x[0]) // 2), ((y[1] + y[0]) // 2, y[1]))
  else:
    if c < (y[0] + y[1]) // 2: # 제 3분면 안에 들어오는 경우
      val += ((2 ** (n - 1)) ** 2) * 2
      recursion(n - 1, ((x[1] + x[0]) // 2, x[1]), (y[0], (y[1] + y[0]) // 2))
    else: # 제 4분면 안에 들어오는 경우
      val += ((2 ** (n - 1)) ** 2) * 3
      recursion(n - 1, ((x[1] + x[0]) // 2, x[1]), ((y[1] + y[0]) // 2, y[1]))

recursion(N, (0, length), (0, length))