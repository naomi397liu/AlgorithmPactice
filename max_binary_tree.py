class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        return the root node
        """
        def helper(nums):
           
            if nums != []:
                threshold = nums.index(max(nums))
                current = TreeNode(max(nums))
            
                
                left = nums[0:threshold]
                right = nums[threshold+1:]
                
                if left != []:
                    
                    current.left = helper(left )
                
              
                if right != []:
                
                    current.right = helper(right)
                
                
        
            return current
       
        return helper(nums)
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        
        """
        if nums:
            i = nums.index(max(nums))
            current = TreeNode(max(nums))
            
            left = nums[:i]
            right = nums[i+1:]
            if left:
                current.left = self.constructMaximumBinaryTree(left)
            if right:
                current.right = self.constructMaximumBinaryTree(right)
        return current