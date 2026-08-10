"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        size=len(intervals)
        # if size==0:
        #     return False
        if size==0 or size==1:
            return True
        i,j=0,1
        while j<size:
            if intervals[i].end>intervals[j].start:
                return False
            i+=1
            j+=1
        return True


