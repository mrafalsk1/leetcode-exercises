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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def _build_tree(nums) -> Optional[TreeNode]:
            if not nums:
                return None
            mid = len(nums) // 2
            tree = TreeNode(nums[mid])
            tree.right = _build_tree(nums[mid + 1 :])
            tree.left = _build_tree(nums[:mid])
            return tree

        return _build_tree(nums)


s = Solution()
nums = [-10, -3, 0, 5, 9]

nums1 = [3, 5, 8]
s.sortedArrayToBST(nums1)
