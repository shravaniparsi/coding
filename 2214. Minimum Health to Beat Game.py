class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # here the minimum is the sum of all damages + 1 inorder to win
        # max damage you can avoid is - 2 cases
        # if armour is greater - we can reduce max(damage)
        # if armour is less - we can renduce armour
        
        return sum(damage) + 1 - min(max(damage),armor)
        
