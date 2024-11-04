matrix = []
string = ""

for _ in range(0, 5):
  word = input()
  matrix.append(word)

longest = max(matrix, key=len)

for col in range(0, len(longest)):
  for row in range(0, len(matrix)):
    if col > (len(matrix[row]) - 1):
      continue
    else:
      string += matrix[row][col]

print(string)