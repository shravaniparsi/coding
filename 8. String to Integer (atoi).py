class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        number, until_first_digit, sign = 0, True, 1  # until_first_digit denotes we have not seen any number, sign is -1 or 1
        for c in s:
            if until_first_digit:
                if c == ' ': continue  # ignore the leading whitespace
                elif c == '-': sign = -1  # final answer is a negative number
                elif c.isdigit(): number = int(c)  # the first digit of number
                elif c != '+': return 0  # the first char is not a digit and not in (' ', '+', '-'), so s is invalid
                until_first_digit = False  # the first char is a digit or '+' or '-', valid number starts
            else:
                if c.isdigit():
                    number = number * 10 + int(c)
                    if sign * number > MAX: return MAX
                    elif sign * number < MIN: return MIN
                else: break   # end of valid number
        return sign * number  # sign is 1 or -1 
        
