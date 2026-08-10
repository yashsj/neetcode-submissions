class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def is_Palindrome(s,i,j)->bool:
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True


        while i<j:
            # if not (is_english_alnum(s[i])) and not (is_english_alnum(s[j])):
                # return False
            if s[i]!=s[j]:
                return is_Palindrome(s, i+1,j) or is_Palindrome(s,i,j-1)
            i+=1
            j-=1
        return True
        

        