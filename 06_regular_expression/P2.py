# Find the words with exactly 8 letters from paragraph using regex
import re

paraString = 'Hello, My name is Aksh Maradiya. i am from junagadh'
findEightLetter = re.findall('[a-zA-Z]{8}', paraString)
print (findEightLetter)