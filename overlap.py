from typing import Tuple

#a = [x1, x2] # x1 < x2
#b = [x3, x4] # x3 < x4


# simple logic to determine if a and b overlap with each other?
def overlap(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    return ( a[0] < b[1] ) and ( a[1] > b[0] )

assert overlap((1, 5), (2, 4)) == True
assert overlap((2, 4), (1, 5)) == True
assert overlap((6, 8), (1, 3)) == False
assert overlap((0, 2), (4, 5)) == False
