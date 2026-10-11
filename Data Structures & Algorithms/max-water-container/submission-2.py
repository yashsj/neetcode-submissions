class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        2 pointer->left, right
        width=right-left
        height=min(h[l],h[r])

        """

        left=0
        right=len(heights)-1
        ans=0
        while left<right:
            height=min(heights[left],heights[right])
            width=right-left
            area=height*width
            ans=max(area,ans)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return ans