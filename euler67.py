# Maximum path sum II
# Problem 67

# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with
# one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not
# possible to try every route to solve this problem, as there are 299
# altogether! If you could check one trillion (1012) routes every second it
# would take over twenty billion years to check them all. There is an
# efficient algorithm to solve it. ;o)

import time

start = time.time()

# First, we'll load up the data file into our tree variable
tree = []
with open('euler67_triangle.txt', 'r') as f:
    content = f.readlines()
tree = [[int(n) for n in x.split()] for x in content if len(x) > 0]

# We need to build up a maximal sum for each node in the tree, by building up
# from the bottom.
# Start with each of bottom row, where maximum is itself.
# Go up a row.
# For each value in the new row, add the value to the child with the highest value.
# Repeat for every row ... when we get the top, we have our answer

last_row = []
for row in tree[::-1]:
    if len(last_row) == 0:
        last_row = list(row)
    else:
        for i in range(len(last_row)-1):
            last_row[i] = row[i] + (last_row[i+1] if last_row[i+1] > last_row[i] else last_row[i])
        last_row.pop() # we're getting shorter by one each time

result = last_row[0]
            
print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
