count = 0
sum = 0
print(count, sum)
for i in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + i
    print(count, sum, i)
print(count, sum, sum / count)