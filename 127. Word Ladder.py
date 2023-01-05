from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #edge cases
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        # To traverse from beginWord to endWord we can do a BFS 
        # we first make a dictionary with each word from wordList 
        # as key with all possible words by replacing each with '*'
        # and value as orginal word eg: h*t = [hot,hit]
        
        # creating a defaultdict with list as type
        possiblewordsdict = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                possiblewordsdict[word[:i] + "*" + word[i+1:]].append(word)
        
        # creating a queue for BFS with one node beginword and 1 as count
        qu = deque([(beginWord,1)])
        # To keep track of visited nodes
        visited = set()
        # setting beginword as visited
        visited.add(beginWord)
        
        # BFS
        
        while qu:
            currword, count = qu.popleft()
            for i in range(len(currword)):
                intermediateword = currword[:i] + "*" + currword[i+1:]
                # h*t -> [hot]
                possiblewords = possiblewordsdict[intermediateword]
                for s in possiblewords:
                    if s == endWord:
                        return count+1
                    if s not in visited:
                        qu.append((s,count+1))
                        visited.add(s)
        return 0
        
