import re
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        l=0
        n=len(tokens)
        while(l<n):
            ch=tokens[l]
            # if ch.isdigit():
            #     stack.append(ch)
            if re.fullmatch(r'[+-]?\d+',ch):
                stack.append(int(ch))

            else:
                op2=stack.pop()
                op1=stack.pop()
                if ch =='+':
                    stack.append(op1+op2)
                elif ch =='-':
                    stack.append(op1-op2)
                elif ch =='*':
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))
            l+=1
        return stack.pop()
        #TC:O(N)
        #SC:O(N)
        

        