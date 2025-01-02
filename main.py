integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def removeOdd(numbers):
#iterate through the list of numbers and remove the odd numbers which module 2 is not equal to 0
    for num in numbers:
        if num % 2 != 0:
            numbers.remove(num)
    return numbers

print(removeOdd(integers), "\n")

set1 = {"apple", "banana", "cherry", "orange", "kiwi", "melon"}
set2 = {"google", "microsoft", "apple", "banana", "orange", "kiwi", "melon"}

def findCommon(set1, set2):
#find the common elements in the two sets using ready intersection function
    common = set1.intersection(set2)
    return common

print(findCommon(set1, set2), "\n")

dict = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
    "key4": 4,
    "key5": 5,
    "key6": 6,
    "key7": 7,
}

def revDict(dictionary):
#reverse the key-value dictionary by iterating through the dictionary and creating a new dictionary with the values as keys and keys as values
    newDict = {}
    for key, value in dictionary.items():
        newDict[value] = key
    return newDict

print(revDict(dict), "\n")

tup = ('Javascript', 56, 3.14, True, 'Python', 7, 3.14, 'Javascript', 7)

def countTypes(tup):
#count the number of each type in the tuple by creating a dictionary with type-number pairs
    types = {}
    for item in tup:
        if type(item) in types:
            types[type(item)] += 1
        else:
            types[type(item)] = 1
    return types

print(countTypes(tup), "\n")

#convert the tuple to a list, add 'CSS', 'HTML', 8, 9 to the list, remove 3.14, 7, 'Javascript' from the list and convert the list back to a tuple
tup = list(tup)
tup.append('CSS')
tup.append('HTML')
tup.append(8)
tup.append(9)
tup.remove(3.14)
tup.remove(7)
tup.remove('Javascript')
tup = tuple(tup)

print(tup)
