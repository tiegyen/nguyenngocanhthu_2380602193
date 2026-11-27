print("Enter the text (Input 'done' to finish):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    print("\nYour text after input then change into uppercase:")
    for line in lines:
        print(line.upper())