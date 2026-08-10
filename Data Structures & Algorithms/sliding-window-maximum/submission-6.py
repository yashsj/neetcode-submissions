class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque()
        l=r=0
        ans=[]
        length=len(nums)
        while(r<length):
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            queue.append(r)
            if queue[0]<l:
                queue.popleft()
            if r-l>=k-1:
                ans.append(nums[queue[0]])
                l+=1
            r+=1
        return ans

