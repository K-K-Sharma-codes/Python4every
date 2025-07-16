count = dict()
names = ["Kunal", "Amit", "Kunal", "Arun", "Amit"]
for i in names:
    if i not in names:
        count[i] = 1
    else:
        count[i] = count[i] + 1
print(count)