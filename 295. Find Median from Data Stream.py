class MedianFinder:
    #IDEA : 
    # To calculate the median, we can maintain divide array into subarray equally:
    # small and large. All elements in small are no larger than any element in large. So median 
    #would be (largest in small + smallest in large) / 2 if small's size = large's size.
    # If large's size = small's size + 1, median is smallest in large.
    # we will have 2 heaps small and large
    # if an element is less than the largest in small w
    # we push to small else to large
    # once we do that we balance number of elements in small and large 
    # i.e if small has more we will take the largest from small and add to largest
    def __init__(self):
        self.small=[]
        self.large=[]
    
    def addNum(self, num: int) -> None:
        # initially if both has no elements
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if num <= -self.small[0]:
            # push to small part
            heapq.heappush(self.small, -num)
        else:
            # push to large part
            heapq.heappush(self.large, num)
        # adjust small and large balance
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))



    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2.0
        return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
