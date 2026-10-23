class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        dq=deque()
        for i in range(len(nums)):
            #keep a sliding window and remove the first element from the left if its out of bounds
            if dq and dq[0]<=i-k:
                dq.popleft()
            # while dq exists and right most elements can be deleted if smaller than nums or curr in the array 
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)

            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans

        
        
        