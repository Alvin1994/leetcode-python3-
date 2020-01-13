class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return digits
        dictChr = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        digits = list(digits)
        rst = [x for x in dictChr[digits.pop(0)]]
        self._letterCombinations(digits, dictChr, rst)
        return rst
    def _letterCombinations(self, digits, dictChr, rst):
        if not digits:
            return 
        nextStrs = dictChr[digits.pop(0)]
        i = len(rst)
        while i > 0:
            curtStr = rst.pop(0)
            for nextStr in nextStrs:
                rst.append(curtStr + nextStr)
            i = i - 1
        return self._letterCombinations(digits, dictChr, rst)