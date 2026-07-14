from array import *

val = array('i',[1,2,3,4,5,6])

# For total no.of iteration

for i in range(0, len(val)):
    print(val[i], end = "")

print('\n')

# For adding ', ' in them

for x in val:
    print(x, end=", ")
print(val.typecode)

print('\n')

# For reversing the array
val.reverse()

for i in range(0 ,len(val)):
    print(val[i], end= " ")

print('\n')

#Insertion in array

val.insert(1, 50)
for i in range(0, len(val)):
    print(val[i], end=" ")

print('\n')

# Appending an array
val.append(100)
for i in range(0, len(val)):
    print(val[i], end=" ") 

print('\n')

# Replace value in array
val[2] = 200
for i in range(0 , len(val)):
    print(val[i], end=" ")

print('\n')

# Making array from same array
val = array('i',[1,2,3,4,5,6,7,8,9])

copyArray = array(val.typecode, (x * 3 for x in val))

for i in range(0, len(val)):
    print(copyArray[i], end=" ")

print('\n')

# Deleting element

val = array('i',[1,2,3,4,5,6,7,8,9])

copyArray = array(val.typecode, (x * 3 for x in val))
copyArray.pop(3)

for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")

print('\n')

# Removing element

for i in range(0, len(copyArray)):
    print(copyArray[i], end =" ")

print('\n')

# Slicing
val = array('i',[1,2,3,4,5,6,7,8,9])
abc = val[2:5]
for i in range(0, len(abc)):
    print(abc[i] ,end=" ")
print("\n")

# Elements added by user

arr = array('i', [])

n = int(input("Enter a number"))

for i in range(0 ,n):
    arr.append(int(input("Enter next input")))

for x in arr:
    print(x, end=" ")

print("\n")

# Searching an element

arr = array("i", [12,23,34,45,56,67,78,89,99])

i = arr.index(45)

print(i)