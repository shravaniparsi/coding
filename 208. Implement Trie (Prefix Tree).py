class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        # self.maxLen = 0

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        # self.maxLen = max(self.maxLen, len(word))
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # if len(word) > self.maxLen:
        #     return False
            
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        
        return True
