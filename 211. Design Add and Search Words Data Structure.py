class TrieNode:
    def __init__(self):
        self.letters={}
        self.endofword=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.letters:
                current.letters[c]=TrieNode()
            current = current.letters[c]
        current.endofword=True
        

    def search(self, word: str) -> bool:
        def dfs(i,root):
            curr = root
            for j in range(i,len(word)):
                c = word[j]
                if c != '.':
                    if c not in curr.letters:
                        return False
                    curr = curr.letters[c]
                else:
                    for val in curr.letters.values():
                        if dfs(j+1,val):
                            return True
                    return False
            return curr.endofword
        return dfs(0,self.root)
        
                
                
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
