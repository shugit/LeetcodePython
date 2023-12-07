class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
      if endWord not in wordList:
        return 0
      pattern = defaultdict(set)

      for word in wordList+[beginWord]:
        for j in range(len(word)):
          p=word[:j] + "*" + word[j+1:]
          pattern[p].add(word)
      print(pattern)
      step = 1
      visited = set([beginWord])
      q = deque([(beginWord, 1)])
      while q:
        for i in range(0, len(q)):
          word, step = q.popleft()
          if word == endWord:
            return step
          for j in range(len(word)):
            p = word[:j] + "*" + word[j+1:]
            for neiWord in pattern[p]:
              if neiWord not in visited:
                visited.add(neiWord)
                q.append((neiWord, step + 1))
      return 0