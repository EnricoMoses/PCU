def my_function():
    global var, var2
    var = 2
    var2 = 10
    print("Do I know that variable?", var)


var = 1
var2 = 9
print(var)
my_function()
print(var)
print(var2)