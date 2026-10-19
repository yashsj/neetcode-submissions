class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        ans=0
        hashset=set()
        while j<len(s):
            if s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            else:
                hashset.add(s[j])
                ans=max(ans,len(hashset))
                j+=1
        return ans



        