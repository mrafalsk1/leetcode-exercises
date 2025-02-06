# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head
        while ahead and ahead.next:
            head = head.next
            ahead = ahead.next.next

        return head
