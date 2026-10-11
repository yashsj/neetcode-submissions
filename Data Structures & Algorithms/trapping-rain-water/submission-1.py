class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        
        ans=0
        while left<right:
            if leftmax<=rightmax:
                left+=1
                curr=leftmax-height[left]
                if curr>0: 
                    ans+=curr
                leftmax=max(leftmax,height[left])
            else:
                right-=1
                curr=rightmax-height[right]
                if curr>0:
                    ans+=curr
                rightmax=max(rightmax,height[right])
        return ans

        