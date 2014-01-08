# Integer right triangles
# Problem 39

# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import time

start = time.time()

result = 0
max_solutions = 0
max_p = 120

def num_integer_right_triangles_with_perimeter(p, debug=0):
    solutions = 0
    for a in range(3,p//3):
        for b in range(a,(p-a)//2):
            if a**2 + b**2 == (p-a-b)**2:
                if debug >= 2: print('p={}, [{},{},{}]'.format(p,a,b,p-a-b))
                solutions += 1
    if debug >= 1: print ('p={}, found {} solutions'.format(p,solutions))
    return solutions

print (num_integer_right_triangles_with_perimeter(120,2))

for p in range(12,1001):
    if p % 100 == 0: print ('Executing for p = {}'.format(p))
    solutions = num_integer_right_triangles_with_perimeter(p)
    if solutions > max_solutions:
        max_solutions = solutions
        result = p

print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
