class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we can do dfs, at each step we determine if it is equal to target, if greater we will return
        # say [2,3,6,7] we start at with [],0,0 from 0(current index to end) we do dfs
        # [2],2,0 
        # [2,2],4,0 [2,3],5,0 [2,6],5,0 [2,7],5,0
        # [2,2,2],6,0 [2,2,3] 7,0 [2,2,6] 10,0 [2,2,7],11,0, [2,3,6],10,0, [2,3,7],12,0, [2,6,7],15,0
        ans = []
        n=len(candidates)
        def dfs(cur,cur_sum,cur_idx):
            if cur_sum>target:
                return
            if cur_sum == target:
                ans.append(cur)
            for i in range(cur_idx,n):
                dfs(cur+[candidates[i]],cur_sum+candidates[i],i)
            
        dfs([],0,0)
        return ans
        
