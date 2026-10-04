class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            charArr=[0]*26
            for char in word:
                charArr[ord(char)-ord('a')]+=1
            key=tuple(charArr)
            res[key].append(word)
        return list(res.values())
                

        