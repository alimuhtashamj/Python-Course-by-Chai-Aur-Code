
grade = int(input('Enter your score(1-100):'))
if not 1<= grade <= 100:
    print("Invalid Input")    
else:
    if grade >=90:
      print("Your grade is A")
    elif grade >=80:
      print("Your grade is B")
    elif grade >=70:
      print("Your grade is C")
    elif grade >= 60:
      print("Your grade is D")
    else:
      print("You failed. Your grade is F")
      pass 
  