# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
#         a**2 + b**2 = c**2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

target = 1000
result = 0
def is_pythagorean(a,b,c):
    return a**2 + b**2 == c**2

for a in range(1,501):
    for b in range(a+1,501):
        c = target - b - a
        if is_pythagorean(a,b,c):
            result = a*b*c
            break
    if result > 0:
        break

print ('Product of special pythagorean triplet is {}'.format(result))
