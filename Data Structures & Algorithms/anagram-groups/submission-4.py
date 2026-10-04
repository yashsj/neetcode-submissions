class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """O(N(klogk))
        (0,0,1,0)

        [act] [cat]
        {a:1,c:0,t:1}
        """
        hashMap=defaultdict(list)
        for word in strs:
            charMap=[0]*26
            for c in word:
                i=ord(c)-ord('a')
                charMap[i]+=1
            key=tuple(charMap)
            hashMap[key].append(word)

        return list(hashMap.values())




        