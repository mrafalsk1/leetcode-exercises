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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _dsf(node: Optional[TreeNode], sum: int):
            if not node:
                return False
            sum += node.val
            if sum == targetSum:
                return True
            if _dsf(node.left, sum):
                return True
            if _dsf(node.right, sum):
                return True
            return False

        return _dsf(root, 0)


s = Solution()
root = [5, 4, 8, 11, 13, 4, 7, 2, 1]
targetSum = 22
