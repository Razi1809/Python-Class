number=[]
for i in range (10):
    num=int(input(f"Enter a number{i+1}:"))
    number.append(num)
print("The complete list: ", number)
print("Total number of elements:", len(number))