class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        ans=0
        # steps=[0*n for _ in range(n+1)]
        # steps[0]=1
        # steps[1]=1
        prev=1
        last=1
        for i in range(2,n+1):
            ans=prev+last
            prev=last
            last=ans

        
        return ans
        #TC:O(N)
        #SC:O(1)

        

        