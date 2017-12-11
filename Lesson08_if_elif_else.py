# Here, we ask if x is greater than y first. 5 is not greater than 10, so this is False.
#  So the elif runs to ask if x is less than z. 
#  In this case, it is asking if 5 is less than 22. 
#  It is, so we will see a print out saying x is less than z. 
#  The "else" part of this will not run. 
x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')
else:
    print('if and elif never ran...')
# Here, we ask if x is greater than y first. 
# 5 is not greater than 10, so this is False. 
# So the elif runs to ask if x is greater than z. 
# In this case, it is asking if 5 is greater than 22. 
# This is false, so it does not run. 
# Then, we find ourselves at the else statement, which notifies us that
#  'if and elif never ran...'
x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x > z:
    print('x is greater than z')
else:
    print('if and elif never ran...')
