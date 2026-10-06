class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            res+=str(len(word))+"$"+word
        print(res)
        return (res)


    def decode(self, s: str) -> List[str]:
        "5$Hello5$World"
        "100$!@#$%^&*()"
        result=[]
        i=0
        while i<len(s):
            """if s[i]=="$":
                print(s[:i])
            else:
                i+=1"""  
            j=i
            while s[j]!="$":
                j+=1
            l=int(s[i:j])
            result.append(s[j+1:j+l+1])
            i=l+j+1
        return result


