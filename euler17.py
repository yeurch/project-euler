# Number letter counts
# Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.

import time

start = time.time()

def verbalise_number(n):
    digits = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
              'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen')
    tens = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    
    if n == 1000:
        return 'one thousand'
    result = ''
    if n >= 100:
        result = digits[n // 100] + ' hundred '
        n = n % 100
        if n > 0:
            result += 'and '
    if n >= 20:
        result += tens[n // 10]
        n = n % 10
        if n > 0:
            result += '-'
    if n > 0:
        result += digits[n]

    return result

result = 0
for x in range(1,1001):
    result += len(verbalise_number(x).replace(' ','').replace('-',''))

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
