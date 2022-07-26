"""#O(sqrt(n))"""
"""class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num+1)
             if i * i = num 
                return true
             if i * i> num
             return False
             """
class Solution:
    def isPerfectSquare(self ,num: int) ->bool:
        low,high = 1,num
        while low <= high:
            mid = (low + high) // 2
            if mid * mid > num:
                 high = mid - 1
            elif mid * mid < num:
                 low = mid + 1
            else:
                return True
        return False
        
    

        
        