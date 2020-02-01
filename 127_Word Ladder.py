from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if not endWord or not wordList or endWord not in wordList:
            return 0
        
        memo = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                memo[word[:i] + '*' + word[i+1:]].append(word)
        visited = {beginWord:True}
        stack = [(beginWord,1)]
        while stack:
            w, c = stack.pop(0)
            for i in range(len(w)):
                for word in memo[w[:i] + '*' + w[i+1:]]:
                    if word == endWord:
                        return c + 1
                    if word not in visited:
                        stack.append((word,c+1))
                        visited[word] = True
        return 0
 
    def ladderLength3(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        def check(queue, visit, otherVisit):
            node, level = queue.pop(0)
            for i in range(L):
                intermediateWord = node[:i] + '*' + node[i+1:]
                for word in intermediateDict[intermediateWord]:
                    if word in otherVisit:
                        return level + otherVisit[word]
                    if word not in visit:
                        queue.append((word,level+1))
                        visit[word] = level + 1
            return None
        if not endWord or endWord not in wordList or not wordList:
            return 0
        L = len(beginWord)
        intermediateDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                intermediateDict[word[:i] + '*' + word[i+1:]].append(word)
        visit_begin = {beginWord: 1}
        visit_end = {endWord: 1}
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        ans = None
        while queue_begin and queue_end:
            ans = check(queue_begin, visit_begin, visit_end)
            if ans:
                return ans
            ans = check(queue_end, visit_end, visit_begin)
            if ans:
                return ans
            
        return 0
                
            