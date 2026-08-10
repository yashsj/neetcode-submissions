class Solution:
    def climbStairs(self, n: int) -> int:
       ans=0
       if n==1 or n==0:
        return 1
       ans+=self.climbStairs(n-1)+self.climbStairs(n-2)
       return ans
    


        