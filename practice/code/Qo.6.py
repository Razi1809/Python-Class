list=[2, 5, 6, 7, 9, 10]
find= int(input("Enter a number: "))
if find in list:
    print("The number ispresent in the list.")
    print("Index:", list.index(find))
else:
    print("Number is not in the list.")
