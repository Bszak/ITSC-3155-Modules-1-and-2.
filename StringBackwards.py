print('Enter a string and behold the magic: ')

a = input()

b = a.swapcase()

c = b[::-1]
def removeSpace(c):
    return c.replace(" ", "")

print(removeSpace(c))

#Sources used: https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/