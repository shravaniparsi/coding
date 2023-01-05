class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we sort the interval based on start time
        # if an interval start time falls before the end of previous interval, then we can merge them
        # the end time of new merge is max of end times of both intervals
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        result = []
        for interval in sorted_intervals:
            start = interval[0]
            end = interval[1]

            if result and start<=result[-1][1]:
                result[-1][1] = max(end,result[-1][1])
            else:
                result.append(interval)
        return result
            
        
