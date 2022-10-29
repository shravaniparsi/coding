# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # we solve this using divide and conquer approch
        # we first apply merge to (1,2) (3,4) sorted lists then again we merge result of the (1,2) and (3,4)
        
        # now we write merge logic for 2 sorted lists
        
        def merge2lists(l1,l2):
           # initialisting head node
            head = ListNode()
        # initially tail and heads are same
            tail = head
        
        # continue comparing elements until there are nodes in both l1 and l2
            while l1 and l2:
                # if node in l1 is less than l2 
                # appending l1 node to the list
                # else l2 node to the list
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                # after appending moving the tail pointer
                tail = tail.next

            # after comparing there might be few elements left in either l1 or l2 
            # that case we attatch them to the tail of list
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2

            return head.next
        
        #edge cases
        
        if not lists:
            return

        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2

        leftHalf = self.mergeKLists(lists[:mid])
        rightHalf = self.mergeKLists(lists[mid:])
        return merge2lists(leftHalf, rightHalf)
            
        
        
        
       
    
        
        
        
        
