list=[1,2, 4, 5, 5, 6, 3, 5, 9, 9]
frequency={}
for num in list:
    if num in frequency:
        frequency[num]= frequency[num]+1
    else:
        frequency[num]=1
for key in frequency:
    print(key, "->", frequency[key])