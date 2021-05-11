class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        if root.right and root.left:
            if (root.val >= low and root.val <= high): 

                return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
            else:
                return self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        
        elif root.right:
            if (root.val >= low and root.val <= high):

                return root.val + self.rangeSumBST(root.right, low, high)
            else:
                return self.rangeSumBST(root.right, low, high)
        
        elif root.left:
            if (root.val >= low and root.val <= high):
                return root.val + self.rangeSumBST(root.left, low, high)
            else:
                return self.rangeSumBST(root.left, low, high)
        
        elif root.val >= low and root.val <= high:
            return root.val
        else:
            return 0