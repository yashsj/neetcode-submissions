class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Heap
        """
        heap=[]
        hashmap=defaultdict(int)
        for n in nums:
                hashmap[n]+=1
        
        #size=0
        for key,value in hashmap.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)

        ans=[]
        while heap:
            pair=heapq.heappop(heap)
            ans.append(pair[1])
        
        return ans
        #O(nlogk)
        #O(n+k)
        """
        #Bucket sort
        arr=[[] for i in range(len(nums)+1)]
        hashmap=defaultdict(int)
        ans=[]
        for n in nums:
            hashmap[n]+=1
        for key,value in hashmap.items():
            arr[value].append(key)
        for i in range(len(nums),-1,-1):
            if arr[i]:
                for a in arr[i]:
                    ans.append(a)
                    if len(ans)==k:
                        return ans
        return ans






            



