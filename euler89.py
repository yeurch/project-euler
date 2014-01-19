# Roman numerals
# Problem 89

# The rules for writing Roman numerals allow for many ways of writing each
# number (see About Roman Numerals...). However, there is always a "best" way of
# writing a particular number.
#
# For example, the following represent all of the legitimate ways of writing the
# number sixteen:
#
#     IIIIIIIIIIIIIIII
#     VIIIIIIIIIII
#     VVIIIIII
#     XIIIIII
#     VVVI
#     XVI
#
# The last example being considered the most efficient, as it uses the least
# number of numerals.
#
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
# contains one thousand numbers written in valid, but not necessarily minimal,
# Roman numerals; that is, they are arranged in descending units and obey the
# subtractive pair rule (see About Roman Numerals... for the definitive rules
# for this problem).
#
# Find the number of characters saved by writing each of these in their minimal
# form.
#
# Note: You can assume that all the Roman numerals in the file contain no more
# than four consecutive identical units.


import time

start = time.time()

values = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def to_decimal(roman):
    result = 0
    roman = roman.upper()
    for x in range(len(roman)):
        if x < len(roman)-1 and values[roman[x]] < values[roman[x+1]]:
            result -= values[roman[x]]
        else:
            result += values[roman[x]]
    return result

def express_digit(digit, one, five, ten):
    if digit == 0:
        return ''
    if digit == 4:
        return one + five
    if digit == 9:
        return one + ten
    result = ''
    if digit >= 5:
        result += five
    result += one * (digit % 5)
    return result

def to_roman(decimal):
    thousands,decimal = divmod(decimal,1000)
    hundreds,decimal = divmod(decimal,100)
    tens,units = divmod(decimal,10)
    
    result = 'M' * thousands
    result += express_digit(hundreds,'C','D','M')
    result += express_digit(tens,'X','L','C')
    result += express_digit(units,'I','V','X')
    return result

numbers = list(open('euler89_roman.txt','r'))
numbers = [x.strip() for x in numbers]

result = 0
for number in numbers:
    result += len(number)
    result -= len(to_roman(to_decimal(number)))


print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
