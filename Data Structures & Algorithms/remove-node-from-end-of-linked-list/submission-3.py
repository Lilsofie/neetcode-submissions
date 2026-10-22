# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0;
        cur = head
        while cur != None:
            count += 1
            cur = cur.next
        
        cur = head
        prev = None
        while cur != None:
            if count == n:
                if prev == None:
                    if cur.next != None:
                        return cur.next
                    return None
                if cur.next == None:
                    prev.next = None
                else:
                    prev.next = cur.next
                return head
            count -= 1
            prev = cur
            cur = cur.next