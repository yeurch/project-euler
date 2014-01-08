# Lattice paths
# Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#    RRDD
#    RDRD
#    RDDR
#    DRRD
#    DRDR
#    DDRR
# How many such routes are there through a 20×20 grid?

import time
start = time.time()

result = 0

# Until such time as we've reached 20 selections, we have 2^20 possibilities
# Then, the remaining 20 selections depend on the availability of Ds and Rs.

# We have 40 choices, so there are 40! ways of arranging them.
# Each different arrangement has 20! arrangements for down and 20! arrangements
# for right, giving (20!)^2 possibilities or each particular layout.
# Simply divide one by the other.

from math import factorial

side_length = 20

moves = side_length * 2
sl_fact = factorial(side_length)
moves_fact = factorial(moves)

result = moves_fact // sl_fact**2

print ('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
