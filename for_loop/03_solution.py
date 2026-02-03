# multiplication table with skipping the 5th iteration
number = 7 
for i in range(1,11):
    if i == 5:
        continue 
    print(number, '*', i , '=', number * i)
    