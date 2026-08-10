class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=list()
        r=len(temperatures)-1
        ans=[0]*len(temperatures)
        while(r>=0):
            while stack and temperatures[stack[-1]]<=temperatures[r]:
                stack.pop()
            if not stack:
                ans[r]=0
                stack.append(r)
            else:
                # ans.insert(0,stack[-1]-r)
                ans[r]=stack[-1]-r
                stack.append(r)
            r-=1
        return ans
        #TC:O(N)
        #SC:O(N)-->may also ask O(1)