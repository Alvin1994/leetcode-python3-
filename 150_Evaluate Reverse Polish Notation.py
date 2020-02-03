class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return tokens
        stack = []
        operator = ['+','*','-','/']
        for ele in tokens:
            if ele not in operator:
                stack.append(int(ele))
            else:
                valA, valB, = stack.pop(), stack.pop()
                if ele == '+':
                    stack.append(valB+valA)
                elif ele == '-':
                    stack.append(valB-valA)
                elif ele == '*':
                    stack.append(valB * valA)
                elif ele == '/':
                    if valA == 0:
                        return 
                    if valA * valB < 0:
                        stack.append(-(-valB//valA))
                    else:
                        stack.append(valB//valA)
        return stack.pop()