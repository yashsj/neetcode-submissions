class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        lmax,rmax = 0,n-1
        ans=0
        while l<r:
            if height[l]<height[r]:
                if height[l]<height[lmax]:
                    ans+=height[lmax]-height[l]
                else:
                    lmax=l
                l+=1
        
            else:
                if height[r]<height[rmax]:
                    ans+=height[rmax]-height[r]
                else:
                    rmax=r
                r-=1
        return ans
