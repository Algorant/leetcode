'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

Write the code that will take a string and make this conversion given a number of rows.
'''

# s is string, r is number of rows

def convert(s, r):
    #base case
    if r == 1:
        return s

    res = [''] * r
    row_idx = 1
    increasing = True

    for c in s:
        res[row_idx-1] += c
        if row_idx == r:
            increasing = False
        elif row_idx == 1:
            increasing = True

        if increasing:
            row_idx += 1
        else:
            row_idx -= 1

    return "".join(res)
