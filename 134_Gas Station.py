class Solution:
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
        if not gas or not cost or len(gas) != len(cost):
            return -1
        
        l,r = 0, len(gas) - 1
        total = gas[r] - cost[r]
        while l < r:
            if total < 0:
                r -= 1
                total += gas[r] - cost[r]
            else:
                total += gas[l] - cost[l]
                l += 1
        return r if total >= 0 else -1
        
#         start = len(cost)-1
#         end = 0
#         sum = gas[start] - cost[start]
#         while start > end:
#             if sum >= 0:
#                 sum += gas[end] - cost[end]
#                 end += 1
#             else:
#                 start -= 1
#                 sum += gas[start] - cost[start]
#         return start if sum >=0 else -1