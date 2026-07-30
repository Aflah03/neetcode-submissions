"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        minHeap = []
        ans = 0
        for  interval in intervals:
            start = interval.start
            end = interval.end
            while minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
            ans = max(len(minHeap), ans)
        return ans


            