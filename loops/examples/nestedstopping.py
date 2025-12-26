numbers = [5, 14, 21, 28, 19, 35]
result = 0 
for i in numbers:
    if i > 20 and i%7 == 0 :
        result = i 
        break 
print(result)