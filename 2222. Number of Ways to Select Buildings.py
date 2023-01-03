class Solution:
    def numberOfWays(self, s: str) -> int:
# basic idea: 
# To obtain '101' we need to find '10' before '1'. 
# Thus, it is necessary to count the number of '10' and '01' before '1' and '0' respectively. 
# Further, we need to count the number of '1' and '0' before '0' and '1' respectively.
        c0=0
        c1=0
        c01=0
        c10=0
        c010=0
        c101=0
        for i in range(len(s)):
            if s[i] == '0':
                c0+=1
                c10+=c1 # += 1's before i
                c010+=c01 # += 01's before i
            else:
                c101+=c10
                c01+=c0
                c1+=1
        return c010+c101

        
