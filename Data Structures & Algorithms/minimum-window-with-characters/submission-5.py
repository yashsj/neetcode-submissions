class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap={}
        tmap={}
        if len(s)<len(t):
            return ""

        for c in t:
            tmap[c]= 1 + tmap.get(c,0)

        have=len(tmap)   
        seen=0
        res=[-1,-1]
        minans=float('infinity') 
        i,j=0,0
        while j<len(s):
            c=s[j]            
            if c in tmap:
                smap[c]=1+smap.get(c,0)
                if smap[c]==tmap[c]:
                    seen+=1
            while i<=j and seen==have:
                if j-i+1<minans:
                    minans=j-i+1
                    res[0],res[1]=i,j+1
                if s[i] in smap:
                    smap[s[i]]-=1
                    if smap[s[i]]<tmap[s[i]]:
                        seen-=1
                i+=1
            j+=1
        
        return s[res[0]:res[1]] if res!=[-1,-1] else ""

        #O(N+M)
        #O(k)
                
            


            