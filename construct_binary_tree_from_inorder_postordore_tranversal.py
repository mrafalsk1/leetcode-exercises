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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = postorder.pop()
        print(inorder)
        print(postorder)
        print(root)
        index_root_inorder = inorder.index(root)
        print(index_root_inorder)

        tree = TreeNode(root)
        tree.right = self.buildTree(inorder[index_root_inorder + 1 :], postorder)
        tree.left = self.buildTree(inorder[:index_root_inorder], postorder)

        return tree


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
s = Solution()
a = s.buildTree(inorder, postorder)
print(a)
