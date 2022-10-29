import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # sort list based on start times
        intervals.sort(key = lambda x: x[0])
        
        #define a heap
        heap = []
        
        for meeting in intervals:
            
            # h=[] is no meeting rooms created 
            # h[0] > meeting[0] is if the top most element in heap is not free
            # i.e the meeting that finishes most early is also not empty
            # we need a new room then add element to heap with its ending time as priority
            if heap == [] or heap[0] > meeting[0]:
                heapq.heappush(heap,meeting[1])
            else:
            # replace the empty room with new meeting end value    
                heapq.heapreplace(heap,meeting[1])
            
        return len(heap)
            
