import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        heap=[]
        for i in s:
            heapq.heappush(heap,(-count[i],i))
        print(heap)
        res=""
        for _ in s:
            n = heapq.heappop(heap)
            print(n)
            res+=n[1]
        return res
