first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

joined_list = []

for x in first_list:
    if x % 2 != 0:
        joined_list.append(x)

for x in second_list:
    if x % 2 == 0:
        joined_list.append(x)

print("Merger list: ", joined_list)

odds = [x for x in first_list if x % 2 != 0]
evens = [x for x in second_list if x % 2 == 0]

merged_list = odds + evens 
print(merged_list)