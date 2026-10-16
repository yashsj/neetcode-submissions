class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        leftmax=height[left]
        rightmax=height[right]
        ans=0
        while left<right:
            if leftmax<=rightmax:
                left+=1
                ans+=max(leftmax-height[left],0)
                leftmax=max(height[left],leftmax)

            else:
                right-=1
                ans+=max(rightmax-height[right],0)
                rightmax=max(height[right],rightmax)
        return ans


