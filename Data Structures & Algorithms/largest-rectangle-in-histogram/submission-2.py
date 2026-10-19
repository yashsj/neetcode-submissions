class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        stack.append((heights[0],0))
        ans=0
        n=len(heights)
        # i,j=0,i+1
        for i in range(1,len(heights)):
            start=i
            while stack and heights[i]<stack[-1][0]:
                h,p=stack.pop()
                ans=max(ans,(i-p)*h)
                start=p
            stack.append((heights[i],start))

        while stack:
                pair=stack.pop()
                ans=max(ans,(n-pair[1])*pair[0])
        return ans
                



