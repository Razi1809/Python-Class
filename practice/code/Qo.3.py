list=[12, 34, 56, 67,70]
total=0
max= list[0]
min=list[0]
for num in list:
    total =total+num
    if num>max:
        max=num
    if num<min:
        min=num
average=total/len(list)
print("sum=", total)
print("average=", average)
print("max=", max)
print("min=", min)