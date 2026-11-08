class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #1)middle partion
        #2)no of elements  left and no of elements right
        #3)left<right-> median(odd/even)
        """
        length=4//2
        9
        9//2
        4, 5
        1 3 5
        4 7 8

        1 3 4 | 5 7 8

        arr 1= 1 | 3 5 -->3//2 = 1
               i  i+1
               l1  r1
        arr 2= 4 7| 8 9
                 j j+1
                 l2 r2

        1 |6 7
        3 4|5 9
        
        1 3 4 5 6 7 9

        1 3 4 | 5 7 8 9

        half= 3
        p=1
        i=p-1
        j=3-1-1
        """
        A,B=nums1,nums2
        n,m=len(A),len(B)
        half=(n+m)//2
        if n>m:
            A,B=B,A
        
        p=len(A)//2
        l,r=0,len(A)-1
        while True:
            i=(l+r)//2
            j=half-i-2

            l1= A[i] if i>=0 else float('-infinity')
            r1= A[i+1] if i+1<len(A) else float('infinity')
            l2= B[j] if j>=0 else float('-infinity')
            r2= B[j+1] if j+1<len(B) else float('infinity')

            if l1<=r2 and l2<=r1:
                if (n+m)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2   
                else:
                    return min(r1,r2)
            
            if l2>r1:
                l=i+1
            else:
                r=i-1
        







