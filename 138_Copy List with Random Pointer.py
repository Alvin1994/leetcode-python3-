"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    # Iterative with O(1) Space
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 
        
        # a->a'->b->b'
        ptr = head
        while ptr:
            copyNode = Node(ptr.val,ptr.next,None)
            ptr.next = copyNode
            ptr = ptr.next.next
        # add random
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        # unweap
        ptr_old, ptr_new = head, head.next
        rst = ptr_new
        while ptr_old:
            ptr_old.next = ptr_old.next.next
            if ptr_new.next:
                ptr_new.next = ptr_new.next.next
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next
        return rst
        
    #BFS
    def copyRandomList2(self, head: 'Node') -> 'Node':
        if not head:
            return 
        stack = [head]
        path = {head:Node(head.val,None,None)}
        while stack:
            curt = stack.pop(0)
            if curt.next:
                if curt.next not in path:
                    path[curt.next] = Node(curt.next.val,None,None)
                    path[curt].next = path[curt.next]
                    stack.append(curt.next)
                else:
                    path[curt].next = path[curt.next]
            if curt.random:
                if curt.random not in path:
                    path[curt.random] = Node(curt.random.val,None,None)
                    path[curt].random = path[curt.random]
                    stack.append(curt.random)
                else:
                    path[curt].random = path[curt.random]
        return path[head]
        
        
     