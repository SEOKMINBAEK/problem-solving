n = int(input())

for _ in range(0, n):
  string = input()
  score = 0
  prev = 0
  
  for c in string:
    prev = prev + 1 if c == 'O' else 0
    score += prev
  
  print(score)