k = int(input())
gems = []

for i in range(2, int(k ** 0.5) + 1):
  while k % i == 0:
    gems.append(i)
    k //= i
  
  i += 1

if k > 1:
  gems.append(k)

print(len(gems))
print(' '.join(str(gem) for gem in gems))