class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        s = 1
        e = len(nums)

        def possible(num):
            st = 0
            en = len(nums)-1
            idx = -1
            while st<=en:
                mid = (st+en)//2
                if nums[mid] >= num:
                    idx = mid
                    en = mid - 1
                else:
                    st = mid + 1
            return idx

        while s<=e:
            mid = (s+e)//2
            idx = possible(mid)
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