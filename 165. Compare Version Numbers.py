class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        i = 0
        j = 0
        while i < len(version1) and j < len(version2):
            i_r = i
            j_r = j
            while i_r < len(version1) and version1[i_r] != '.':
                i_r+=1
            while j_r < len(version2) and version2[j_r] != '.':
                j_r+=1
            if int(version1[i:i_r]) == int(version2[j:j_r]):
                i = i_r+1
                j = j_r+1
                continue
            if int(version1[i:i_r]) > int(version2[j:j_r]):
                return 1
            else:
                return -1
        if i >= len(version1) and j >= len(version2):
            return 0
        if i < len(version1):
            s = version1
            i = i 
            rst = 1
        else:
            s = version2
            i = j
            rst = -1
        while i < len(s):
            i_r = i
            while i_r < len(s) and s[i_r] !='.':
                i_r+=1
            if int(s[i:i_r])>0:
                return rst
            i = i_r + 1
        return 0
            
        