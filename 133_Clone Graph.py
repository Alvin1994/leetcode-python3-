"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 

        stack = [node]
        visit = {node:Node(node.val,[])}
        
        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in visit:
                    new = Node(neighbor.val,[])
                    visit[neighbor] = new
                    stack.append(neighbor)
                visit[n].neighbors.append(visit[neighbor])
        return visit[node]