class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        i = 0
        sumi = 0
        maxi = max(nums)
        while(i<len(nums)):
            sumi += nums[i]
            if sumi < 0:
                sumi = 0
            maxi = max(maxi,sumi)
            i+=1
        return maxi if maxi != 0 else max(nums)