# exec compiles and evalute whatever you pass to it in string form
# example 1: like eval
exec("print('so it works like eval')")
# example 2: exectuting an assertion
list_string = "[1,2,3,4,5]"
list_num = exec(list_string) # returns None
# to actually return the list
exec("list_string2 = '[1,2,3,4,5]'")
print(list_string2)
# example 3: and even functions!
exec("def test(): print('wow!')")
test()
# example 4: multi lines
exec(''' 
def test2():
    print("now this should work as well")
    return 42
 ''')
test2()