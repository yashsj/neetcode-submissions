class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_list=[0]*26
        for c in s:
            arr_list[ord(c)-ord('a')]+=1
        for c in t:
            arr_list[ord(c)-ord('a')]-=1
        
        for i in range(len(arr_list)):
            if arr_list[i]!=0:
                return False
        return True

        
