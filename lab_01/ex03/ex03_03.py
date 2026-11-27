def create_tuple_list(lst):
    return tuple(lst)

input_list = input("Enter a list of integers (separated by commas): ")
numbers = [int(num) for num in input_list.split(",")]

my_tuple = create_tuple_list(numbers)
print("The list created from the input is:", numbers)
print("The tuple created from the list is:", my_tuple)
