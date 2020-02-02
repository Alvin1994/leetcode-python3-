class Solution:
    # XOR, space complexicity = O(1)
    def singleNumber(self, nums: List[int]) -> int:
        rst = 0
        for num in nums:
            rst ^= num
        return rst 
    # HASH TABLE
    def singleNumber2(self, nums: List[int]) -> int:
        if not nums:
            return -1
        hashTable = {}
        for num in nums:
            if num not in hashTable:
                hashTable[num] = 1
            else:
                del hashTable[num]
        return hashTable.popitem()[0]
        