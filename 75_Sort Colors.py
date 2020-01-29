class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        return self.onePass(nums)
    def onePass(self, nums: List[int]) -> None:
        i, rPt, bPt = 0,0,len(nums)-1
        while i < bPt + 1 :
            if nums[i] == 0:
                nums[i], nums[rPt] = numsp[rPt], nums[i]
                rPt += 1
                i += 1 
                continue
            if nums[i] == 2:
                num[bPt],nums[i] = nums[i], nums[bPt]
                bPt -= 1 
                continue
            i +=1
            
        
    def countingSort(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1 
            elif num == 1:
                white += 1
            else:
                blue += 1
        for i in range(0, len(nums), 1):
            if red > 0:
                nums[i] = 0
                red -= 1
                continue
            if white > 0:
                nums[i] = 1
                white -=1
                continue
            nums[i] = 2
        return 