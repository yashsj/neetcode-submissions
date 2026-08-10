class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        size=len(intervals)
        if size==1:
            return intervals
        res=[intervals[0]]
        for start,end in intervals[1:]:
            prevend=res[-1][1]
            if start<=prevend:
                res[-1][1]=max(prevend,end)
            else:
                res.append([start,end])
        return res
        #TC:O(nlogn)
        #SC:O(N) Output array


        