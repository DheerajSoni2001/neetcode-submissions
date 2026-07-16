class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxHeap = []
        ans = []
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i],i))
        ans.append(-maxHeap[0][0])
        i = k
        while i < len(nums):
            heapq.heappush(maxHeap, (-nums[i],i))
            while maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0][0])
            i+=1
        return ans