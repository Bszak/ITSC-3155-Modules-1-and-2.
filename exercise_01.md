grade = int(input('Enter a grade from 0 to 100: '))

if grade >= 90 and grade <= 100:
    print("Your grade is an A. Excellent job!")
elif grade >= 80 and grade <= 89:
    print("Your grade is an B. Not bad at all.")
elif grade >= 70 and grade <= 79:
    print("Your grade is an C. Could be worse, right?")
elif grade >= 60 and grade <= 69:
    print("Your grade is an D. Its time to hit the books next time.")
elif grade < 59:
    print("Your grade is an F. %$@#%")

    #Sources used to help
    # https://www.w3schools.com/python/gloss_python_elif.asp
    # https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/