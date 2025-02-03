formula = input()

divide_subtract = formula.split('-')

result = 0

for i, term in enumerate(divide_subtract):
  tot = sum(map(int, term.split('+')))
  result = result - tot if i else result + tot

print(result)