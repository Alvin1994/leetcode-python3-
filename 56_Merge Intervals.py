class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        assert isinstance(intervals,list)
       
        if not intervals:
            return []
              
        intervals = sorted(intervals, key = lambda x:x[0])
        rst = [intervals[0]]
    
        for interval in intervals[1:]:
            if interval[0] <= rst[-1][-1]:
                rst[-1][-1] = max(rst[-1][-1], interval[-1])
            else:
                rst.append(interval)
        return rst