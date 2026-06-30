class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        s,e=0,len(nums)-1

        while(s<=e):
            mid = (s+e)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
        return s