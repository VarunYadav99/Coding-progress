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
    def guessNumber(self, n):
        l, r = 1, n
        while True:
            m = (l+r)//2
            match guess(m):
                case  0: return m
                case  1: l = m+1
                case -1: r = m-1