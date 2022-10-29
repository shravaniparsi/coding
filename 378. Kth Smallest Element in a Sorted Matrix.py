class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # we declare a heap keep pushing items when it reached k we will pop elements
        heap=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heappush(heap,-matrix[i][j])
                if(len(heap)>k):
                    heappop(heap)
        return -heappop(heap)
