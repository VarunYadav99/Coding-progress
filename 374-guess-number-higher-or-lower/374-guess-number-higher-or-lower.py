# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""class Solution:
    def guessNumber(self, n: int) -> int:
        low, high=1, n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            if res < 0:
                high = mid - 1
                
            elif res > 0:
                low = mid + 1 
            else:
                return mid"""
                

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = (l + r)//2
            if guess(m) == 0: return m
            elif guess(m) == -1:
                r = m - 1
            else:
                l = m + 1
        return l