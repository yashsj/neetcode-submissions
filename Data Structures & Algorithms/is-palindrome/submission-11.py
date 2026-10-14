class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=s.lower()
        i=0
        j=len(s)-1
        while i<j:
            while i<j and not string[i].isalnum():
                i+=1
            while i<j and not string[j].isalnum():
                j-=1
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True

            
            

        