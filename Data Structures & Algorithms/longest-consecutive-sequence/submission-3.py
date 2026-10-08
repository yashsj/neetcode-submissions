class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Sort nums->diff
        O(nlogn)
        """

        """
        [,,,,,,] 
        2 20-->18
        4-->2
        3-->2
        """

        hashset=set(nums)
        ans=0
        for n in hashset:
            if n-1 not in hashset:
                curr=1
                while n+curr in hashset:
                    curr+=1
                ans=max(curr,ans)

        return ans


