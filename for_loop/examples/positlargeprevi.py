numbers = [-1, 2, 3, -4, 5, 6, 1, 7]
count = 0 
for i in range(1, 8):
    if numbers[i] > 0 and numbers[i] > numbers[i-1]:
        count += 1
print('All positive numbers that are larger than the previous number are', count)
