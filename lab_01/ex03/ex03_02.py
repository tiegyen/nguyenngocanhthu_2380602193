def reverse_list(lst):
    return lst[::-1]

input_list = input("Enter a list of integers (separated by commas): ")
numbers = [int(num) for num in input_list.split(",")]
reversed_numbers = reverse_list(numbers)
print("The reversed list is:", reversed_numbers)