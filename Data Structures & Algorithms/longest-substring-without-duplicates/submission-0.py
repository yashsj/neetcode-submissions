class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string=set()
        n=len(s)
        i,j=0,0
        ans=0
        while j<n:
            char=s[j]
            if char not in longest_string:
                longest_string.add(char)
                ans=max(ans,len(longest_string))
                j+=1
            else:
                longest_string.discard(s[i])
                i+=1
        return ans

        
            

        