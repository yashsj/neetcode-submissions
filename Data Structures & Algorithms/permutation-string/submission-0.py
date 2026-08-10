class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        list1=[0]*26
        list2=[0]*26
        for char in s1:
            index=ord(char)-ord('a')
            list1[index]+=1
        
        matches=0
        l=0
        r=0
        length1=len(s1)
        length2=len(s2)

        def checkmatch(list1: list, list2: list,matches :int=0)->int:
            for i in range(len(list1)):
                if list1[i]==list2[i]:
                    matches+=1
            return matches
            
        while r<length2:
            list2[ord(s2[r])-ord('a')]+=1
            if r>=length1-1:
                matches = checkmatch(list1,list2)
                if matches==26:
                    return True
                else:
                    list2[ord(s2[l])-ord('a')]-=1
                    l+=1
            r+=1
        return False
            
            






        