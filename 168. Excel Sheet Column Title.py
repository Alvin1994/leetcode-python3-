class Solution:
    # @return a string
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while n > 0:
            result.insert(0, capitals[(n-1)%len(capitals)])
            n = (n-1) % len(capitals)
        # result.reverse()
        return ''.join(result)