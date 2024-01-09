class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0   # initializing window start to 0.
        end = 0     # initializing window start to 0.
        sm = nums[start]  # variable to keep track of the sum of the particular window.
        minlen = len(nums)  # keeps track of the window length.
        totSum = 0  # keeps track of the total sum of the minlen window.

        while(start<=end and end<len(nums)):
            
            # if the element in the array itself is >= target.
            if nums[end]>=target:
                return 1
            
            # when sum>=target, calculate the window length.
            if sm>=target:
                
                diff = end-start+1
                if diff<=minlen:
                    minlen = diff
                    totSum = sm
                sm = sm - nums[start]
                start = start+1
                
            # when sum<target, expand the sliding window.
            else:
                end = end + 1
                if end<len(nums):
                    sm = sm + nums[end]
                    
        # when the sum of all elements in the array is not >= target.
        if minlen==len(nums):
            if totSum==0:
                return 0
        return minlen
        