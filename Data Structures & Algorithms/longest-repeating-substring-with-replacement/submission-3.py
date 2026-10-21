class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        maxLen=0
        i=0
        j=0
        maxfreq=0
        while(j<len(s)):
            hashmap[s[j]]=1+ hashmap.get(s[j],0)
            maxfreq=max(maxfreq,hashmap[s[j]])
            if(j-i+1)-maxfreq>k:
                hashmap[s[i]]-=1
                i+=1
            maxLen=max(maxLen,j-i+1)
            j+=1

        return maxLen

        
        
