class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        my_dict={'}':'{',')':'(',']':'['}

        for char in s:
                if char in my_dict:
                    if stack and stack[-1]==my_dict[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
                
        return True if not stack else False


       
            
            



            

            