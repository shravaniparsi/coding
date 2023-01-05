class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }
        total = 0
        i = 0
        while i < len(s):
            #if at least 2 symbols remaining AND value of s[i] < value of s[i + 1]:
            #if s[i] is less than s[i+1] we subtract the s[i] from s[i+1]
            #as we traveresed two elements we increment i with 2
            if i+1<len(s) and convert[s[i]] < convert[s[i+1]]:
                total +=  convert[s[i+1]] - convert[s[i]]
                i += 2
            else:
                total +=convert[s[i]]
                i += 1
        return total
        
