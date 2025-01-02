import re
from time import process_time

myStr = "Hello, this is the second assignment of the course of Python Programming, which is named Introduction to Programming two."
#clean the string using regular expression and re library
cleanedStr = re.sub(r'[^\w\s]', '', myStr)
#this function change pattern symbols to empty string, pattern include all non-word non-space non-number characters

print(cleanedStr, '\n')

#counting the vowels by using for loop and compare each character with vowels
vowels = 'aeiou'
countVowels = 0
for i in cleanedStr:
    if i in vowels:
        countVowels += 1

print(countVowels, '\n')

#counting the consonants by using for loop and compare each character with consonants(the same as vowels)
consonants = 'bcdfghjklmnpqrstvwxyz'
countConsonants = 0
for i in cleanedStr:
    if i in consonants:
        countConsonants += 1

print(countConsonants, '\n')

newStr = cleanedStr
word = str(input("Enter word: "))
changeWord = 'Programming'
#changing 'Programming' to entered word
for i in range(len(newStr)):
#check for 'Programming' in our string by choosing more characters using ':'
    if newStr[i:i+len(changeWord)] == changeWord:
#replacing the 'Programming' by our word and piecewise string adding
        newStr = newStr[:i] + word + newStr[i+len(changeWord):]

print(newStr,'\n')

#using split we create a set of words(cause we need unique) and use sorted() for sorting the words
words = set(cleanedStr.split())
words = sorted(words)

print(words,'\n')