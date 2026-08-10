class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        hashmap={}
        maxf,res=0,0
        for right in range(len(s)):
            hashmap[s[right]]=1+hashmap.get(s[right],0)
            maxf=max(maxf,hashmap[s[right]])

            while (right-left+1)-maxf>k:
                hashmap[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res
        