# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        self.deepest = []
        self.deepest = self.helper(root, 0)
        print(self.deepest)
        maximum = 0
        sum_val = 0 
        for tup in self.deepest:
            if tup[1] > maximum:
                maximum = tup[1]
        for tup in self.deepest:
            if tup[1] == maximum:
                sum_val += tup[0]
        return sum_val
        
        
        
    def helper(self, root, depth):
        """
        :type root: TreeNode
        :rtype: int
        
        traverse the tree
        save end values to an array 
        sum array
        """
        # [(7, 4), (5,3), (8, 4)]
        
        if root.right:
            rr = root.right
            self.helper(rr, depth + 1)
        if root.left:
            rl = root.left
            self.helper(rl, depth + 1)
        if not root.left and not root.right:
            self.deepest.append((root.val, depth))
        return self.deepest