class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Level0: []
        level1: [1]                  [2]              [3]
        level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
        level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

        """
        def backtracking(subset):
            if len(subset) == len(nums):
                res.append(subset)
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtracking(subset+[nums[i]])
                    visited.remove(i)
        
        visited = set()
        res = []
        backtracking([])
        return res
