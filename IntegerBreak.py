# Problem can be found here - https://leetcode.com/problems/integer-break/description/ 
def integerBreak(self, n: int) -> int:
    if n == 2: return 1
    if n == 3: return 2
    res = 1
    while n > 0:
        if n - 3 >= 2:
            res *= 3
            n -= 3
        else:
            res*= n
            n -= n
    return res
