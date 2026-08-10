class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap=defaultdict(int)
        smap=defaultdict(int)
        mincount=len(s)
        ans=""
        for c in t:
            tmap[c]+=1
        tcount=len(tmap)
        scount=0
        i,j=0,0
        while j<len(s) or (i<len(s) and scount==tcount):                         
            if scount<tcount and j<len(s):
                c1=s[j]
                if c1 in tmap:
                    smap[c1]+=1
                    if tmap[c1]==smap[c1]:
                        scount+=1
                j+=1

            elif scount==tcount:
                if len(s[i:j])<=mincount:
                    ans=s[i:j]
                    mincount=j-i
                c2=s[i]
                if c2 in tmap:
                    smap[c2]-=1
                    if tmap[c2]>smap[c2]:
                        scount-=1
                i+=1

        return ans
            


                






            
    

        