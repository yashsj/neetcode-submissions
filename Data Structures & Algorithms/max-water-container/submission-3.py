class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        ans=0

        while i<j:
            if heights[i]<heights[j]:
                amt1=min(heights[i],heights[j])*(j-i)
                ans=max(ans,amt1)
                i+=1
            else:
                amt2=min(heights[i],heights[j])*(j-i)
                ans=max(ans,amt2)
                j-=1

        return ans
                

