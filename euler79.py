# Passcode derivation
# Problem 79

# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.

import time

start = time.time()

trios = list(open('euler79_keylog.txt','r'))
trios = [x.strip() for x in trios]
freq = [[0]*10,[0]*10,[0]*10]

for trio in trios:
    for p in range(3):
        freq[p][int(trio[p])] += 1

for i in range(3):
    print(','.join(['{0:02d}'.format(x) for x in freq[i]]))

result = 0

'Computation above assisted with manual solving!'
'The result is 73162890'
# print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
