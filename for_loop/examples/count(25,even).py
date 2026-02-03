numbers = [12, 28, 33, 40, 17, 26, 30, 19]
count25_even = 0 
for i in numbers:
    if i > 25 and i%2 == 0: 
        count25_even += 1 
print('Total Numbers greater than 25 and even are', count25_even)

# i > 25 and i%2 == 0 is not counting separately
# They are both counting: numbers that are greater than 25 AND even
