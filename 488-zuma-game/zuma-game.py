class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_same(s, i):
            if i < 0 :
                return s
            l = r = i
            while l > 0 and s[l - 1] == s[i]:
                l -= 1
            while r + 1 < len(s) and s[r + 1] == s[i]:
                r += 1
            if r - l + 1 >= 3:
                return remove_same(s[:l] + s[r+1:], l - 1)
            else:
                return s
        hand = "".join(sorted(hand))
        q = deque([(board, hand, 0)])
        visited = set([(board, hand)])
        while q:
            curr_b, curr_h, step = q.popleft()
            for i in range(len(curr_b)+1):
                for j in range(len(curr_h)):
                    if j > 0 and curr_h[j-1] == curr_h[j]:
                        continue
                    if i > 0 and curr_b[i-1] == curr_h[j]:
                        continue
                    pick = False
                    if i < len(curr_b) and curr_b[i] == curr_h[j]:
                        pick = True
                    if 0 < i < len(curr_b) and curr_b[i-1] == curr_b[i] and curr_b[i] != curr_h[j]:
                        pick = True
                    if pick:
                        new_b = remove_same(curr_b[:i] + curr_h[j] + curr_b[i:], i)
                        new_h = curr_h[:j] + curr_h[j+1:]
                        if not new_b:
                            return step + 1
                        if (new_b, new_h) not in visited:
                            q.append((new_b, new_h, step + 1))
                            visited.add((new_b, new_h))
        return -1