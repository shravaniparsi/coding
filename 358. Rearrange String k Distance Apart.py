
import collections
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
#         # IDEA: we count frequencies and sort them
#         # pick up highest freq character and arrange them with k gaps and move on with all
#         # characters
        
        n = len(s)
        # edge cases
        if not k: return s
        
        if k==0 or k==1:
            return s
        
        # frequencies
        count = collections.Counter(s)
        
        # if we cannot accomodate the characters rearrangement
        maxf = max(count.values())
        if (maxf - 1) * k + list(count.values()).count(maxf) > len(s):
            return ""
        
        res = list(s)
        
        # we start filling character from (n-1)%k because
        # here k is 4 and if we start at 4th pos
        #---a ---a ---a -a In this case, a would have a gap of 2.
        # so we start at (n-1)%k to distribute chars
        i = (n - 1) % k
        for c in sorted(count, key=lambda i: -count[i]):
            for j in range(count[c]):
                res[i] = c
                i += k
                if i >= n:
                    i = (i - 1) % k
        return "".join(res)
