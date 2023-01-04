class Solution:
    def minimumKeypresses(self, s: str) -> int:
#         Idea: Always make the letters with higher frequency to be easier accessible.
# Say there are 3 letters on one button (left - mid - right). Left is the easiest to access, mid is the second, right is the hardest.
# Steps:
# Sort letter with frequency reversely, then assign each with following orders
# 1-left, 2-left, 3-left, ... 9-left | 9 in total (easiest to access)
# 1-mid, 2-mid, 3-mid, ... 9-mid | 9 in total
# 1-right, 2-right, 3-right, ... 8-right | 8 in total, since at most 26 letters (hardest to access)
        cnts = collections.Counter(s)
        cnts = sorted(cnts.items(), key = lambda x: -x[1])  # desc order
        res = 0
        print(cnts)
        for idx, (key, val) in enumerate(cnts):
            if idx <= 8:
                res += val
            elif idx > 8 and idx <= 17:
                res += 2*val
            else:
                res += 3*val
        return res
        
