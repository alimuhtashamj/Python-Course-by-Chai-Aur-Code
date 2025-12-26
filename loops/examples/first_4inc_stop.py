# Find the first number that is: larger than the previous number
# and the increase is more than 4. Stop immediately after finding it.
num = [3, 6, 8, 9, 15, 14, 20]
count = 0 
for i in range(1,len(num)):
    if num[i] > num[i-1] and (num[i] - num[i-1] > 4):
    #    print immediately before the next loop starts and break it
        print(num[i])
        break
 