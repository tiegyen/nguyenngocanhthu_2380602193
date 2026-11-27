def sum_even(lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum

input_list = input("Enter a list of integers (separated by commas): ")
numbers = [int(num) for num in input_list.split(",")]

total_sum = sum_even(numbers)
print("The sum of even numbers in the list is:", total_sum)