class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        assert isinstance(num1,str) and isinstance(num2,str)
        
        if num1 == '0' or num2 == '0':
            return '0'
        pos = [0] * (len(num1) + len(num2))
        for i, i_val in enumerate(reversed(num1)):
            for j, j_val in enumerate(reversed(num2)):
                pos[i+j] += int(i_val) * int(j_val)
                pos[i+j+1] += pos[i+j] // 10
                pos[i+j] = pos[i+j] % 10
        while pos[-1]==0:
            pos.pop()
        return ''.join(map(str,pos[::-1]))