temperatures = [28, 31, 29, 35, 30, 32, 27]
count = 0 
for temp in temperatures:
    if temp > 30:
        count += 1
print(count, "days were hotter than 30.")