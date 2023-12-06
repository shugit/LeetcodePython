class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for x,y in dislikes:
          graph[x].add(y)
          graph[y].add(x)
        # print(graph)
        colors = [None] * (n+1)
        def dfs(i, color):
          colors[i] = color
          for j in graph[i]:
            if colors[j] == colors[i]:
              return False
            if colors[j] == None and not dfs(j,-color ):
              return False
          return True
        
        for i in range(1, n+1):
          if colors[i] == None and not dfs(i, 1):
            return False
        return True
        