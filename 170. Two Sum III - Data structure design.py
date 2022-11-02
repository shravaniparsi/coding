class TwoSum:

    def __init__(self):
        self.num=[]
        

    def add(self, number: int) -> None:
        self.num.append(number)
        

    def find(self, value: int) -> bool:
        h={}
        for i in self.num:
            if value-i in h:
                return True
            else:
                h[i]=i
            
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
