class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        cursum = 0 
        for n in nums:
            if cursum<0:
                cursum = 0
            cursum+=n
            maxsub=max(maxsub,cursum)
        return maxsub
    
             
        
        
"""        First we find out the maxSum
2. currSum --> 0
3. if we have the currSum less than 0 then we have to set the currSum to 0
4. Then we add the current element to the subarray sub
5. Then we will compare the currSum with the maxSum
6. Finally we will return the maximum maxSum"""



 