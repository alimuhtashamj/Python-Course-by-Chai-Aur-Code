def sum_all(*num):
    print(num)
    for i in num:
        print(i*2)
    return sum(num)
print('Sum of all : ',  sum_all(1,2,3))
