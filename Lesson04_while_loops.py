# In this code, we have defined a variable name condition,
# and condition starts at a value of 1.
condition = 1

while condition < 10:
	print(condition)
	condition += 1
# This setup of a while loop is known as creating a "counter," since basically that
# is what we're doing. We're saying we just want to count 1 for every iteration and
# eventually stop at our limit. While loops are usually finite and defined in this
# sense, but while loops can also be undefined. Something like:
	print(condition)
	condition += 1
# In this case, this loop would continue running while it was raining outside. 
# When the rain stopped, the loop would cease.
while isRaining:
	print(condition)
# If you actually run the following code, you can stop it by doing ctrl+c to break it. 
# The following is an intentional infinite loop
while True:
	print('doing stuff!!')