# remove duplicates from the array (take input int,str)
array=[str(x) for x in input("Enter numbers, separate them with space: ").split()]

store_unique_vlaues=[]

for x in array:
    if x not in store_unique_vlaues:
       store_unique_vlaues.append(x)
print(store_unique_vlaues)
