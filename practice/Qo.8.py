list=[12, 40, 40, 32, 32, 2]
unique=[]
for num in list:
    if num not in unique:
        unique.append(num)
print(unique)