# Coded triangle numbers
# Problem 42

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
# so the first ten triangle numbers are:
#
#           1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
# value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?

import time

start = time.time()

def is_triangle(n):
    low_factor = int((2*n)**0.5)
    return low_factor * (low_factor+1) / 2 == n

def is_triangle_word(word):
    return is_triangle(sum([ord(x)-64 for x in word]))

with open('euler42_words.txt', 'r') as f:
    words = [word.strip('"') for word in f.readline().upper().split(',')]

result = sum([1 for word in words if is_triangle_word(word)])

print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
