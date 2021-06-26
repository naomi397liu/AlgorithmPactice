class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        '''
        get all the numbers out of both trees and then sort them
        
        '''
    
        nums = []
        def helper(node, nums):
            if node:
                if node.left:
                    nums.append(node.left.val)
                    helper(node.left, nums)
                if node.right:
                    nums.append(node.right.val)
                    helper(node.right, nums)
            return nums
        if root1:
            nums.append(root1.val)
            helper(root1, nums)
        if root2:
            nums.append(root2.val)
            helper(root2, nums)
        nums.sort()
        return nums