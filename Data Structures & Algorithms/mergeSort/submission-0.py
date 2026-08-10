# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
         return self.mergeSort_Helper(pairs,0,len(pairs)-1)

    def mergeSort_Helper(self,pairs:List[Pair],s:int,e:int)->List[Pair]:
        
        if e-s+1<=1:
            return pairs
        mid=(s+e)//2
        self.mergeSort_Helper(pairs,s,mid)
        self.mergeSort_Helper(pairs,mid+1,e)
        self.merge(pairs,s,mid,e)
        return pairs

    def merge(self,nums:List[Pair],s:int ,m: int,e:int)->None:
        L=nums[s:m+1]
        R=nums[m+1:e+1]
        i=0
        j=0
        k=s
        while i<len(L) and j<len(R):
            if L[i].key<=R[j].key:
                nums[k]=L[i]
                i=i+1
            else:
                nums[k]=R[j]
                j=j+1
            k=k+1

        while i<len(L):
                nums[k]=L[i]
                i=i+1
                k=k+1
        while j<len(R):
                nums[k]=R[j]
                j=j+1
                k=k+1
        

