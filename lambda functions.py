# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression
# def double(x):
#    return x*2
# print(double(50))

double = lambda x: x*2
multiply = lambda x, y: x*y
add = lambda x, y, z: x + y + z
print(add(5, 60, 13))
