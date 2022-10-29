class Solution:
    def reorganizeString(self, s: str) -> str:
# IDEA:
# First count the number of characters in word.
# If any character is having its presence greater then the half of length of string then it's impossible to arrange them.
# Now, sort the dictionary counter in decreasing order on the basis of its number of times presence in word.
# Start putting the most frequent letter into the resultant list one by one leaving the one space in between.
# for second most frequent first search for the blank space where it started and similarly for others.
        
        #edge case
        if not s:
            return ""
        
        # counting the characters and their frequencies and sorting in decreasing order
        n = len(s)
        dic = Counter(s)
        sorteddic = dict(sorted(dic.items(),key=lambda x: x[1],reverse=True)) 
        
        # if any of character freq is greater than half of length of string -> impossible
        for c in dic:
            if dic[c] > ((len(s)+1)//2):
                return ""
            
        # constructing an array of size of string with all empty spaces marked as '-'
        res = ["-"]*len(s)
        
        # we will start iterating through dict, take most freq and replace them consequently from first empty space found until all chars in string are replaced in res
        
        numofcharstoberearranged = len(s)
        
        while numofcharstoberearranged > 0:
            i = 0
            while res[i]!="-":               # find the start of empty slot.
                i += 1
            for c in sorteddic:
                while i<len(s) and sorteddic[c] > 0:
                    res[i] = c
                    sorteddic[c] -= 1
                    i += 2
                    numofcharstoberearranged -= 1
                
        return ''.join(res)
                
    
        
