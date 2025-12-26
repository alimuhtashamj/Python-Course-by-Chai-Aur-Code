# Count how many times a number is larger than the previous number
numbers = [3, 5, 2, 4, 6, 1, 7]
count = 0 
for i in range(1,len(numbers)):
    if numbers[i]> numbers[i-1]:
        count += 1  
print('Total number of times a number is larger than the previous number is', count)