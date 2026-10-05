class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        char_arr=[0]*26
        for i in range(len(s)):
            char_arr[ord(s[i])-ord('a')]+=1
            char_arr[ord(t[i])-ord('a')]-=1
        
        for n in char_arr:
            if n!=0:
                return False
        return True

        
