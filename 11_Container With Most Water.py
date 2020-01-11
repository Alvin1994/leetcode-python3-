class Solution:
    def maxArea(self, height: List[int]) -> int:
        assert isinstance(height,list)
        l = 0
        r = len(height) - 1 
        max_area = float('-inf')
        while l < r:
            area = (r-l)*min(height[l],height[r])
            max_area = max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area