class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,num*-1)
        if self.maxheap and self.minheap and (self.maxheap[0]*-1)>(self.minheap[0]):
            val=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val*-1)
        if (len(self.maxheap)-len(self.minheap)>1):
            v=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,v*-1)
        if (len(self.minheap)-len(self.maxheap)>1):
            v=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,v*-1)


    def findMedian(self) -> float:
        if not self.maxheap and not self.minheap:
            return float(0)
        elif len(self.maxheap)>len(self.minheap):
            return self.maxheap[0]*-1
        elif len(self.maxheap)<len(self.minheap):
            return self.minheap[0]
        else:
            m1=self.maxheap[0]*-1
            return (m1+self.minheap[0])/2
        #TC:O(N)
        #SC:O(N)
        
        