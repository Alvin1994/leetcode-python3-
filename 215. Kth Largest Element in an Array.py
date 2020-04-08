class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums,len(nums)-k+1)
    
    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if pos + 1 == k:
                return nums[pos]
            if pos+1 < k:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            else:
                return self.findKthSmallest(nums[0:pos], k)

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        i = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[i] = nums[i], nums[l]
                i += 1
            l += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1
        
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)