class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        assert isinstance(digits,list)
        
        i = len(digits)-1
        digits[i] += 1
        
        while i > 0 and digits[i] > 9:
            digits[i-1] += digits[i] // 10
            digits[i] %= 10
            i -= 1
        if digits[0] > 9:
            digits.insert(0,digits[0]//10)
            digits[1] %= 10
        return digits