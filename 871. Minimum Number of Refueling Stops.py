class Solution:
    def minRefuelStops(self, target: int, fuel: int, s: List[List[int]]) -> int:
        heap = [] 
        #including start and end points
        s = [(0, 0)] + s + [(target, 0)]
        n, ans = len(s), 0
                
        # iterating to all stations starting from 1
        for i in range(1,n):
            # to reach 1st station
            fuel -= s[i][0]-s[i-1][0]
            
            # if there's any fuel in heap and requires fuel
            while heap and fuel<0:
                p = -heapq.heappop(heap)
                fuel += p
                # increasing the cnt
                ans += 1
            # if requires fuel and no heap
            if fuel<0:
                return -1
            #add to the heap for usage
            heapq.heappush(heap, -s[i][1])
        return ans
