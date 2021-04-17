'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

def reverse(x):
    #check if negative
    neg_check = 1
    # ignoring negative sign, convert to str
    if x < 0:
        neg_check = -1
        x_str = str(x)[1:]
    # if positive, convert to str
    else:
        x_str = str(x)

    # reverse the str
    x = int(x_str[::-1])

    return 0 if x > pow(2, 31) else x * neg_check
