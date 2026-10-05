class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for word in strs:
            charArr=[0]*26
            for char in word:
                charArr[ord(char)-ord('a')]+=1
            key=tuple(charArr)
            hashMap[key].append(word)
        return list(hashMap.values())


        
        