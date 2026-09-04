"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)
        max_events = 0

        heap = []
        for intr in intervals:
            if len(heap) == 0:
                heapq.heappush(heap, intr.end)
                max_events = max(max_events, len(heap))
                continue
            
            if intr.start >= heap[0]:
                end_t = heap[0]
                while len(heap) > 0 and heap[0] == end_t:
                    heapq.heappop(heap)

            heapq.heappush(heap, intr.end)
            max_events = max(max_events, len(heap))

        return max_events