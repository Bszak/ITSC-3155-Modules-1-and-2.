print("Enter a word: ")
def splitting(string):
    listString = string.split(' ')

    return listString
def joinString(listString):
    string = '-'.join(listString)

    return string

if __name__ == '__main__':
    str1 = input(" ")

    listString= splitting(str1)
    print(listString)

    new_string = joinString(listString)
    print(new_string)

    # Sources used:
    # https://www.geeksforgeeks.org/python-program-split-join-string/
    # unable to finish.