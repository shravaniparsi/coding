class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        res = [ ]
        prefix = ""
        
        # to improve here we can do binary search
        def search(searchWord):
            temp = []
            for prod in products:
                if prod.startswith(searchWord) and len(temp) < 3:
                    temp.append(prod)
            return temp
            
            
        for c in searchWord:
            prefix += c
            # search for words starting with this prefix
            matchedwords = search(prefix)
            res.append(matchedwords)
        return res
            
            
        
