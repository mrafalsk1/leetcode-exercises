# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = reversed_list
            reversed_list = current_node
            current_node = next_node

        return reversed_list
