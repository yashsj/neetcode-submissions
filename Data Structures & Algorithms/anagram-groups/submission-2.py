class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for word in strs:
            charSet=[0]*26
            for char in word:
                index=ord(char)-ord('a')
                charSet[index]+=1
            key=tuple(charSet)
            if key in ans:
                ans[key].append(word)
            else:
                ans[key]=[word]
        return list(ans.values())

