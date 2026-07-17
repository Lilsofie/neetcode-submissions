"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        end = 0
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if end == 0:
                end = interval.end
            else:
                if interval.start < end:
                    return False
                else:
                    end = interval.end
        return True
