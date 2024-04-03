my_array = [29,7, 34, 2,64, 1]
minVal = my_array[0]

for i in my_array:
    if i <= minVal:
        minVal = i

print(minVal)