from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.to_dict().__repr__()

    def to_dict(self):
        return {
            "val": self.val,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)
        while q1 or q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False

            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)

        return len(q1) == 0 and len(q2) == 0
