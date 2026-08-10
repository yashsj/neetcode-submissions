class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapfreq={}
        n=len(s)
        i=j=0
        maxfreq=0
        ans=0
        while j<n:
            char=s[j]
            len_str=j-i+1
            if char in mapfreq:
                mapfreq[char]+=1
            else:
                mapfreq[char]=1
            maxfreq=max(maxfreq,mapfreq[char])
            if not(len_str-maxfreq<=k):
                len_str-=1
                mapfreq[s[i]]-=1
                i+=1

            ans=max(ans,len_str)
            j+=1
        return len_str


            




        