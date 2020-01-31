# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder or not inorder:
            return
        
        def helper(preorder, inorder):
            if not inorder:
                return None
            
            head = TreeNode(preorder[0])
            i = 0
            while inorder[i] != preorder[0]:
                i += 1
            head.left = helper(preorder[1:1+i], inorder[0:i])
            head.right = helper(preorder[i+1:], inorder[i+1:])
            return head
        return helper(preorder,inorder)
        
        
        
        
        
        
#     def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
#         if not preorder or not inorder:
#             return 
#         root = TreeNode(preorder[0])
#         self._buildTree(preorder, inorder, root)
        
#         return root
#     def _buildTree(self, preorder: 'List[int]', inorder: 'List[int]', node:'TreeNode') -> 'TreeNode':
#         lenOfLeft = 0
#         while inorder[lenOfLeft] != node.val and lenOfLeft < len(inorder):
#             lenOfLeft += 1
#         lenOfRight = len(inorder) - lenOfLeft - 1 
#         if lenOfLeft:
#             node.left = TreeNode(preorder[1])
#             self._buildTree(preorder[1:1+lenOfLeft],inorder[0:lenOfLeft],node.left)
#         if lenOfRight:
#             node.right = TreeNode(preorder[lenOfLeft+1])
#             self._buildTree(preorder[lenOfLeft+1:], inorder[lenOfLeft+1:],node.right)
#         return 
        
        
        
        
        
        
   
            