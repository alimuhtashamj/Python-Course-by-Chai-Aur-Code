numbers = [3, -6, -9, 12, -15, 7, -4]
negative_div_by_3 = 0 
for i in numbers:
    if i < 0 and i%3 == 0:
        negative_div_by_3 += 1 
print('Total numbers which are negative and divisble by 3 are', negative_div_by_3)
         
    