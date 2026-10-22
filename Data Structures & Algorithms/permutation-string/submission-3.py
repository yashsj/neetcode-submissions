class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        arr1=[0]*26
        arr2=[0]*26
        for s in s1:
            arr1[ord(s)-ord('a')]+=1
        print(arr1)

        i=0
        j=0
        
        count=0
        while j-i+1<=len(s1):
            arr2[ord(s2[j])-ord('a')]+=1
            j+=1
            count+=1
        print(j)
        while j<len(s2):
                if  arr1==arr2:
                    return True
                arr2[ord(s2[i])-ord('a')]-=1
                i+=1
                arr2[ord(s2[j])-ord('a')]+=1
                j+=1
        return arr1==arr2
                





              