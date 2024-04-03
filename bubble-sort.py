my_array = [64, 34, 25, 12, 22, 11, 90, 5]

number_of_reps = len(my_array)

for i in range(number_of_reps - 1):
    swapped = False
    for j in range(number_of_reps-i-1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
    if not swapped:
        break

print(my_array)