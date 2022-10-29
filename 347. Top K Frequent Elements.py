class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creating dictionary to store counts
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        # we will create a heap with - so that it's maxheap (python constructs minheap by default)
        heap = []
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key], key))
        
        # now we will pop k elements from heap
        res = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        
        return res
