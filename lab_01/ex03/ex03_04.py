def access_elements(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Enter a tuple of integers (1,2,3): "))
first, last = access_elements(input_tuple)

print("The first element of the tuple is:", first)
print("The last element of the tuple is:", last)