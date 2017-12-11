# grouping some basic caltulation functions under the class calculator
class calculator:
    # first function
    def addition(x,y):
        added = x + y
        print(x, '+', y, '=', added)
    # second function
    def subtraction(x,y):
        sub = x - y
        print(x, '-', y, '=', sub)
    # third function
    def multiplication(x,y):
        mult = x * y
        print(x, '*', y, '=', mult)
    # forth function
    def division(x,y):
        div = x / y
        print(x, '/', y, '=', div)

# some example for using the different funtions within the class:
calculator.subtraction(5,8)

calculator.multiplication(3,5)

calculator.division(5,3)

calculator.addition(5,2)

