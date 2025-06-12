# find the largest number in an array

array=[int(x) for x in input("Enter numbers, separate them with space: ").split()]
sorted_array= sorted(array)
largest_ele=sorted_array[-1]
print(largest_ele)