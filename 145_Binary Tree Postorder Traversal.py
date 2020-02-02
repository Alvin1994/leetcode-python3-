# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rst = []
        def helper(node,rst):
            if not node:
                return 
            
            helper(node.left, rst)
            helper(node.right, rst)
            rst.append(node.val)
            return 
        helper(root,rst)
        return rst
    
    ## ref dasheng2 bellow
    
    # 1. The first is by postorder using a flag to indicate whether the node has been visited or not.
#     def postorderTraversal(self, root):
#         traversal, stack = [], [(root, False)]
#         while stack:
#             node, visited = stack.pop()
#             if node:
#                 if visited:
#                     # add to result if visited
#                     traversal.append(node.val)
#                 else:
#                     # post-order
#                     stack.append((node, True))
#                     stack.append((node.right, False))
#                     stack.append((node.left, False))

#         return traversal

    # 2. The 2nd uses modified preorder (right subtree first). Then reverse the result.
#     def postorderTraversal(self, root):
#         traversal, stack = [], [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 # pre-order, right first
#                 traversal.append(node.val)
#                 stack.append(node.left)
#                 stack.append(node.right)

#         # reverse result
#         return traversal[::-1]
        
        