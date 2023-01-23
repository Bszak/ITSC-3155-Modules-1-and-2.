print("Enter a number for the first list: ")
list1 = []
list2 = []
list3 = []

for n in range(5):
    list1.append(int(input()))

print("Enter numbers for the second list please: ")
for n in range(5):
    list2.append(int(input()))

for n in list1:
    if n in list2:
        list3.append(n)
print("First list: ", list1)
print("Second list: ", list2)
print("Common List: ", list3)

#Sources used: https://www.w3schools.com/python/ref_list_append.asp
# Help within the Discord for code. Code explained:
# It asks for an integer value to be inputed from the first list in a range of 5 integers.
# Then, it asks for a second list, same process as before.
# For the common list, the n varaible is used to go through both list 1 and list 2 to
# grab common variables that are then appended to the back of a list and printed.

