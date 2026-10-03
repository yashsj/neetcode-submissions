class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charArr=[0]*26
        for i in range(len(s)):
            charArr[ord(s[i])-ord('a')]+=1
            charArr[ord(t[i])-ord('a')]-=1
        
        for val in charArr:
            if val!=0:
                return False
        return True
            