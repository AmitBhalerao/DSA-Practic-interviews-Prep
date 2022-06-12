# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #return will be maximum of rob and notrob value at root or current node
        #return type is [rob,notrob] values
        return max(self.TreeHouseRobbery(root))
    
    def TreeHouseRobbery(self,root:Optional[TreeNode])->list[int]:
        
        if root==None:
            return [0,0]
        
        left_subtree = self.TreeHouseRobbery(root.left)
        right_subtree = self.TreeHouseRobbery(root.right)
        
        rob = root.val + left_subtree[1] + right_subtree[1]  #taking subtree notrob value
        notrob = max(left_subtree) + max(right_subtree)
        
        return [rob,notrob]
