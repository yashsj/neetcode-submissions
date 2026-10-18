class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
[(40,5),(28,6)]
"""
        stack=[]
        ans=[0]*len(temperatures)
        for i,t in enumerate(temperatures):

            while stack and stack[-1][0]<t:
                pair=stack.pop()
                ans[pair[1]]=i-pair[1]
            
            stack.append((t,i))
        
        return ans

        #O(N)
        #O(N)
                



