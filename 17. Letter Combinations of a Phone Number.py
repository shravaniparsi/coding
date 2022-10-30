class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #IDEA: we do dfs and print all combinations
        if not digits: return []
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        result = []

        def dfs(seq, current):                  # given sequence of digits, generate combination
            if not seq:                         # if sequence become empty, 
                result.append(current)          # - append the current combination
                return

            for letter in dict[seq[0]]:         # for each letter in first-digit-letters
                dfs(seq[1:], current+letter)    # - merge letter with current comb, then repeat for next digits

        dfs(digits, "")                         # start with full sequence and empty combination
        return result
        
