# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if not inorder or not postorder:
            return 
        
        root = TreeNode(postorder[-1])
        i = 0
        while inorder[i] != postorder[-1]:
            i += 1
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right =self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
#     def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
#         if not inorder or not postorder:
#             return []
#         root = TreeNode(postorder[-1])
#         self._buildTree(root,inorder,postorder)
#         return root
        
#     def _buildTree(self, node, inorder, postorder) -> 'TreeNode':
#         rootIndex_inorder = inorder.index(postorder[-1])
#         lenOfLeftSubTree = rootIndex_inorder
#         lenOfRightSubTree = len(inorder)-lenOfLeftSubTree-1
        
#         if lenOfLeftSubTree > 0:
#             node.left = TreeNode(postorder[lenOfLeftSubTree-1])
#             self._buildTree(node.left,inorder[0:rootIndex_inorder],postorder[0:lenOfLeftSubTree])
        
#         if lenOfRightSubTree > 0:
#             node.right = TreeNode(postorder[lenOfLeftSubTree+lenOfRightSubTree-1])
#             self._buildTree(node.right,inorder[rootIndex_inorder+1:],postorder[lenOfLeftSubTree:lenOfLeftSubTree+lenOfRightSubTree])

#         return