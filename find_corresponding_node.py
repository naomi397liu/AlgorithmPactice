from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        '''
        return the equivalent node in the cloned tree
        edge case: what if there are repeated values so you cannot find the node based on value alone
        
        '''
       
        to_be_seen = deque([cloned])
        while to_be_seen:
            current_node = to_be_seen.popleft()
            if current_node.val == target.val:
                return current_node
            if current_node.right:
                to_be_seen.append(current_node.right)
            if current_node.left:
                to_be_seen.append(current_node.left)