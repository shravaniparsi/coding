class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #For example, if we have 4 letters A in our tasks and n = 3, then minimum window looks like A...A...A...A. So, the minimum length in this case we need is 13 = (n+1) * 3 + 1
        # If we have other task which also has same highest frequency then it should be like
        #Then we need to have window A...A...A...A and also window B...B...B...B, and you can not put one inside another. So, in this case we need at least one symbol more, and example will be AB..AB..AB..AB.
        # hence here we need + 1 more , i.e for each element with highest freq +1 increases
        freq = Counter(tasks)
        Most_freq = freq.most_common()[0][1]
        Found_most = sum([freq[key] == Most_freq for key in freq])
        return max(len(tasks), (Most_freq - 1) * (n + 1) + Found_most)
