"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        i,j=0,0
        count=0
        res=0
        size=len(intervals)
        while j<size:
            if i<size and start[i]<end[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res=max(count,res)
        return res
            




        