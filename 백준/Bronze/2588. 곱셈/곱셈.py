value1 = int(input())
value2 = input()

result1 = value1 * int(value2[2])
result2 = value1 * int(value2[1])
result3 = value1 * int(value2[0])
sum = result1 + (result2 * (10 ** 1)) + (result3 * (10**2))

print(result1)
print(result2)
print(result3)
print(sum)