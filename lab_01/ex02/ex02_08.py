def divisible_by_5(binary_number):
    decimal_number = int(binary_number, 2)
    if decimal_number % 5 == 0:
        return True
    else:
        return False
binary_string = input("Enter the binary number (separated by commas): ")

binary_list = binary_string.split(",")
divisible_numbers = [num for num in binary_list if divisible_by_5(num)] 

if len(divisible_numbers) > 0:
    result = ", ".join(divisible_numbers)
    print("The binary numbers that are divisible by 5 are:", result)
else:
    print("No binary numbers are divisible by 5.")