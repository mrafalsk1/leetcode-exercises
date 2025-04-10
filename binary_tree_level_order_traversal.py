from collections import deque
from typing import List, Optional


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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = [[root.val]]

        while q:
            lvl_size = len(q)
            lvl = []
            while lvl_size != 0:
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl_size -= 1
            res.append(lvl)
        return res
