"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = 0
        end = 0
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if start == 0 and end == 0:
                start = interval.start
                end = interval.end
            else:
                if interval.start < end:
                    return False
                else:
                    start = interval.start
                    end = interval.end
        return True
