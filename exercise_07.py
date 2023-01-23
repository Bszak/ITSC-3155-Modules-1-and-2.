array1 =[]
num = 0

while True:
    currentInput = input("Enter a number or QUIT to quit: ")
    if currentInput == "QUIT":
        break
    array1.append(currentInput)
    while(num < len(array1)):
        if array1[num] % 2 ==0:
            num+= 1



print("All nums: ", array1)
print("All even nums: " , num)

#Sources for help
# https://www.quora.com/How-do-you-write-a-Python-program-that-takes-inputs-from-the-user-until-q-is-entered-Do-you-have-to-make-a-list-from-user-inputs
# Code explained: While the array is true for an input, it will keep asking for a number until you submit "QUIT", then the program stops
# - and breaks, printing the output of all the numbers inputed within the array.
# Couldn't figure out how to implent even while printing out all nums. All nums work if you delete lines 9-11.
