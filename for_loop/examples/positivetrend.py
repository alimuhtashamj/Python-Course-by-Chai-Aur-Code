# Count how many times a number is larger than the previous number,
# but ignore all comparisons where either number is negative.
num = [-3, 1, 4, -2, 5, 7, -1, 8]
count = 0
for i in range(1,len(num)):
    if num[i-1] < 0 or num[i] < 0:
        continue 
    if num[i] > num[i-1]:
        count += 1
print(count)