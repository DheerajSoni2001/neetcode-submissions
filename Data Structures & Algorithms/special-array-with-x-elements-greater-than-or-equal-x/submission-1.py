import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        s = 1
        e = len(nums)

        while s<=e:
            mid = (s+e)//2
            idx = bisect.bisect_left(nums, mid)
            if idx == -1:
                elements = 0
            else:
                elements = len(nums)-idx
            if elements==mid:
                return mid
            elif elements > mid:
                s = mid + 1
            else:
                e = mid - 1
        return -1