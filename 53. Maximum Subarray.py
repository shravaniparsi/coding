class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        msum =a[0]
        csum = a[0]

        for i in range(1,len(a)):
            csum = max(a[i], csum + a[i])
            msum = max(msum,csum)

        return msum
        # iterative approch
        # msum = 0
        # if len(nums)==0:
        #     msum= 0
        # elif len(nums)==1:
        #     msum= nums[0]
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         csum = sum(nums[i:j])
        #         msum = max(msum,csum)
        # return msum
        

        
