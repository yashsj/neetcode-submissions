class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary=defaultdict(list)
        for word in strs:
            arr=[0]*26
            for c in word:
                arr[ord(c)-ord('a')]+=1
            dictionary[tuple(arr)].append(word)

        return list(dictionary.values())
        #O(N*m)
        #O(N*m)
            

        
            