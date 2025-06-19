# max product of two integer in a list
numbers=[int(x) for x in input("Enter numbers, separate using space...").split()]
sorted_numbers=sorted(numbers)
if len(numbers)<2:
    print("Error! Require atleast two integers.")
else:
    # calculate two largest number
    max_product_1= sorted_numbers[-1]*sorted_numbers[-2]
    max_product_2= sorted_numbers[0]*sorted_numbers[1]
    result=max(max_product_1,max_product_2)
    print(result)