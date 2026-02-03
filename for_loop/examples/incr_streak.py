# Count how many times a number continues an increasing streak of at least 3 consecutive increases.
numbers = [2, 4, 6, 5, 7, 9, 11, 3, 6, 8]
streak= 0
count = 0 
for i in range(1,len(numbers)):
    if numbers[i] > numbers[i-1]:
        streak += 1 
        #here nested if conditional can be used as well
        #and then the reset is done in the end
    else:
        streak = 0
    if streak >= 3:
            count += 1
print(count)
    