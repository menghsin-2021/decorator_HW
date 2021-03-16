#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jason
#
# Created:     16/03/2021
# Copyright:   (c) jason 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def debug_divide(func):
    def inner(n, d):
        if d != 0:
            return func(n, d)
        else:
            return 0
    return inner


@debug_divide
def divide(n, d):
    return n / d

k = divide(1, 4)
print(k)
k = divide(1, 0)
print(k)