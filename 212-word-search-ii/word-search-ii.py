
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                    node = node.children[c]
                node.is_end = True
            return root
        root = build_trie(words)
        m = len(board)
        n = len(board[0])
        res = set()
        visited = set()
        def bt(i, j, node, word):
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in visited or board[i][j] not in node.children:
                return 
            visited.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.is_end:
                res.add(word)
            for dire in directions:
                bt(dire[0]+i, dire[1]+j, node, word)
            visited.remove((i,j))

        for i in range(0, m):
            for j in range(0,n):
                bt(i, j, root, "")
        return list(res) 