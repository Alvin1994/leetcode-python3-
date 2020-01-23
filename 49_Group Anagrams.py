class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        assert isinstance(strs, list)
        if not strs:
            return 
        rst = dict()
        for s in strs:
            if ''.join(sorted(s)) not in rst:
                rst[''.join(sorted(s))] = [s]
                continue
            rst[''.join(sorted(s))].append(s)
        return rst.values()
            