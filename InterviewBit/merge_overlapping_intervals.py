# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def insert_intervals(intervals, value):
    inserted = False
    for i in range(len(intervals)):
        if value.start >= intervals[i].start and value.start  <= intervals[i].end:
            if value.end > intervals[i].end:
                intervals[i].end = value.end
            inserted = True
            break
        elif value.end >= intervals[i].start and value.end <= intervals[i].end:
            if value.start < intervals[i].start:
                intervals[i].start = value.start
            inserted = True
            break
    if not inserted:
        intervals.append(value)
    return intervals
    
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        final_intervals = []
        if len(intervals) > 0:
            final_intervals.append(intervals[0])
        for interval in intervals[1:]:
            final_intervals = insert_intervals(final_intervals, interval)
        
        second_final = []
        final_intervals.sort(key=lambda x: x.start)
        if len(final_intervals) > 0:
            second_final.append(final_intervals[0])
        for interval in final_intervals[1:]:
            second_final = insert_intervals(second_final, interval)
        return second_final
