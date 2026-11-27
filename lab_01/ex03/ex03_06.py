def remove_elements(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_remove = 'b'
result = remove_elements(my_dict, key_to_remove)
if result:
    print(f"Key '{key_to_remove}' has been removed from the dictionary.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
print("Updated dictionary:", my_dict)