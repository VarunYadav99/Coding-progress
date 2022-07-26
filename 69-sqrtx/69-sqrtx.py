class Solution:
	def mySqrt(self, num: int) -> int:
		start = 0
		end = num
		while start <= end:
			mid = start+(end-start)//2
			if mid*mid == num:
				root = mid
				break

			if mid*mid > num:
				end = mid-1
			else:
				start = mid+1
				root = mid
		return root
"""    class Solution:
def mySqrt(self, x: int) -> int:
     s=1,e=x

    while s<=e:
        mid=(s+e)//2
        p=mid**2
        if p==x:
            return mid
        elif p>x:
            e=mid-1
        else:
            s=mid+1
    return e"""