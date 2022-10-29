import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # creating dictionary with counts
        count={}
        for word in words:
            if word in count:
                count[word] +=1
            else:
                count[word]=1
        # constructing max heap by giving negative values
        # by default python constructs minheap
        heap=[]
        for key in count:
            heapq.heappush(heap,(-count[key],key))
        
        # now popping k elements from heap and appending to result
        res =[]
        for _ in range(k):
            n = heapq.heappop(heap)
            res.append(n[1])
        return res
            
        
        
