class Solution:
    def trap(self, height: List[int]) -> int:
        
        # for every single position, the amount of water that could be trapped is 
        # we calculate max left and max right 
        # minimum of max left and max right - height at that position.
        
        #edge cases
        if height is None or len(height) == 0:
            return 0
        
        # initially trappedwater is 0
        trappedwater = 0
        
        # we calculate all max left heights and max right heights at each position
        
        leftheight = [0] * len(height)
        rightheight = [0] * len(height)
        
        leftheight[0] = height[0]
        rightheight[-1] = height[-1]
        
        for i in range(1,len(height)):
            leftheight[i] = max(leftheight[i-1],height[i])
               
        for i in range(len(height)-2,-1,-1):
            rightheight[i] = max(rightheight[i+1],height[i])
        
        for i in range(len(height)):
            trappedwater += min(leftheight[i],rightheight[i]) - height[i]
            
        return trappedwater
        
        
        
# O(N) time complexity and space complexity
