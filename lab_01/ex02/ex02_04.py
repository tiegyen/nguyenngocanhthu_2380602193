i = []

for j in range(2000, 3201):
    if (j % 7 == 0) and (j % 5 != 0):
        i.append(str(j))
print(','. join(i))