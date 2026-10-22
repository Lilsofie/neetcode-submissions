# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        new, temp, cur = head, head, head
        idx, count = 0, 0
        values = []
        while cur != None:
            if idx == 0:
                values.append(cur.val)
                cur = cur.next
                count += 1
            elif idx % 2 == 1:
                temp.next = ListNode()
                temp = temp.next
            else:
                values.append(cur.val)
                temp.next = cur
                temp = temp.next
                cur = cur.next 
                count += 1  
            idx += 1

        idx = -1
        cur = head
        temp = new
        
        while cur != None:
            if temp.val == 0:
                temp.val = values[idx] 
                idx -= 1
            count -= 1
            if count == 0:
                temp.next = None
                head = new
            temp = temp.next
            cur = cur.next

        
          
