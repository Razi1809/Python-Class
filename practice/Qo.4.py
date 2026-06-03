list=[12, 30, 43, 60, 71, 80]
even_count= 0
odd_count= 0
for num in list:
    if num%2==0:
        even_count=even_count+1
    else:
        odd_count= odd_count+1
print("Number of even elements= ", even_count)
print("Number of odd elements= ", odd_count)