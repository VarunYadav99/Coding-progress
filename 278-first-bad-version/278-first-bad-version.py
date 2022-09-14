# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):    # checking if the first one in bad
            return 1
        l = 1                  # now the left one is good
        r = n                  # and the right one is bed
        while r-l > 1:         # As soon as they became neighbors we return the right one
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r