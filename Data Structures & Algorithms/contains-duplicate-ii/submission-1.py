class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set_nums=set()
        length=len(nums)
        l,r=0,0
        while r<length:
            n=nums[r]
            if r-l<=k:
                if n in set_nums:
                    return True
                set_nums.add(n)
                r+=1
            else:
                set_nums.discard(nums[l])
                l+=1
        return False