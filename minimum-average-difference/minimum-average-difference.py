class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre_sum=[]
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            pre_sum.append(pre)
        max_sum=pre_sum[-1]
      
        min_dif=float('+inf')
        idx=0
        n=len(nums)
        for i in range(len(nums)):
            if i!=n-1:
                present=(pre_sum[i]//(i+1)) -((max_sum-pre_sum[i])//(n-i-1))
            else:
                present=pre_sum[i]//(i+1)
            
            present=abs(present)
            if present<min_dif:
                idx=i
                min_dif=present
            
        return idx
        