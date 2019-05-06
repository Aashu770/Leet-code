# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val                                         #Nodes are added here 
            t1.left = self.mergeTrees(t1.left, t2.left)             #the left node of t1 and left node of t2 are added here by recursive
            t1.right = self.mergeTrees(t1.right, t2.right)           #the right node of t1 and right node of t2 are added here by recursive
    
        return output