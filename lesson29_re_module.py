import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''
ages = re.findall(r'\d{1,3}',exampleString) # find 1-3 digits
names = re.findall(r'[A-Z][a-z]*', exampleString) # find capital letter follows by 0 or more lower case letters

print(ages)
print(names)
# ziping the two lists into one dictionary
ageDict = dict(zip(names,ages))
print(ageDict)