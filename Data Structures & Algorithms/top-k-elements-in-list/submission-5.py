class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        min_heap=[]
        result=[]
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num]=1
        for num,freq in frequency.items():
            heapq.heappush(min_heap,(freq,num))
            #if we have size of the heap > k, then just pop
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        for freq,num in min_heap:
            result.append(num)
        return result
        

