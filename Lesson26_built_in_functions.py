# Absolute value: Distance from 0
exNum1 = -5
exNum2 = 5

print(abs(exNum1)) # 5
if abs(exNum1) == exNum2:
    print('those values are equal')
# Help function: Opens a Help Menu or a specific function (or you can just use google)
# Best run on Python Terminal (ide)
help() # help menu
help(print) # specificaly for the print function
# Minimum and Maximum
exList = [3,4,5,6,7,8,]
print(min(exList)) # 3
print(max(exList)) # 8
# Rounding a number (there are also floor and ceil rounding in the Math module)
x = 5.622
print(round(x)) # 6
x = 5.222
print(round(x)) # 5
# Converting Data Types
intMe = '55'
print(int(intMe)) # converts to the intger number 55
print(float(intMe)) # converts to the float number 55.0
strMe = 77
print(str(strMe)) # converts to the string '77'
