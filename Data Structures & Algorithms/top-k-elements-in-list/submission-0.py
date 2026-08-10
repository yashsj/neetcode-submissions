class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap=[]
        hashmap={}
        for num in nums:
            hashmap[num]=1+hashmap.get(num,0)
        for num in hashmap.keys():
           heapq.heappush(minheap,(hashmap[num],num))
           if len(minheap)>k:
                heapq.heappop(minheap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        
        