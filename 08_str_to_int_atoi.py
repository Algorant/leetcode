'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
'''

def myAtoi(s):
    # use regex pattern
    match = re.match(r'^\s*([+|-]?\d+)', s)

        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))

        return 0
