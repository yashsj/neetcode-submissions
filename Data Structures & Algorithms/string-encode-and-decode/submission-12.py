class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string=encoded_string+str(len(s))+"#"+s
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        decoded=list()
        j=0
        while j<len(s):
            n=""
            while s[j].isdigit():
                n+=s[j]
                j+=1
            d=int(n)
            decoded.append(s[j+1:j+1+d])
            j=j+1+d
        return decoded

