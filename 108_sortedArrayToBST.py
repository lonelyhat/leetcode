# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree_helper(start, end):
            if(start == end):
                return None
            mid = (start+end)//2
            root = nums[mid]
            root_node = TreeNode(root)
            root_node.left = tree_helper(start,mid)
            root_node.right = tree_helper(mid+1,end)
            return root_node
        return tree_helper(0,len(nums))
