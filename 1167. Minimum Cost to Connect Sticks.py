class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #IDEA: heapify the sticks, get the first minimum combine them and ppush it back
        # continue until only one element in heap
        # eacch time you push increase the cost
        if len(sticks)==0:
            return 0
        
        heap=sticks
        heapq.heapify(heap)
        
        cost = 0
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            cost += x + y
            heapq.heappush(heap, x + y)
        return cost
            
