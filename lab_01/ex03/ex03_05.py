def occurences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_string = input("Enter a string of characters, separated by space: ")
word_list = input_string.split()

occurences_times = occurences(word_list)
print("The occurrences of each character in the string are:", occurences_times)