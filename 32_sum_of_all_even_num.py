# sum of all even number in an array
numbers = [int(x) for x in input("Enter elements of array: ").split()]
sum_even = sum(num for num in numbers if num % 2 == 0)
print(f"The sum of even numbers in the array is: {sum_even}")