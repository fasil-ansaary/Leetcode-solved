import math as m
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+','-','*','/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                if i == '+':
                    v3 = v1 + v2
                    stack.append(v3)
                elif i == '-':
                    v3 = v2 - v1
                    stack.append(v3)
                elif i =='*':
                    v3 = v1 * v2
                    stack.append(v3)
                elif i == '/':
                    if v1 < 0 and v2 < 0:
                        v3 = v2/v1
                    elif v1 < 0 or v2 < 0:
                        v3 = -1*(abs(v2)/abs(v1))
                    else:
                        v3 = v2/v1
                    stack.append(v3)
        return stack.pop()
