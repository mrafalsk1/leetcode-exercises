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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder(root, result)

        return result

    def _inorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


node3 = TreeNode(3)
node2 = TreeNode(2, node3)
root = TreeNode(1, None, node2)
s = Solution()
a = s.inorderTraversal(root)
print(a)
