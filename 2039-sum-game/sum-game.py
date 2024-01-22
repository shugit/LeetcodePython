class Solution:
    def sumGame(self, num: str) -> bool:
        q = 0
        s = 0
        for i in range(len(num)//2):
            if num[i] == '?':
                q += 1
            else:
                s += int(num[i])
        q2 = 0
        s2 = 0
        for i in range(len(num)//2, len(num)):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])
        diff = s - s2
        q_diff = q2 - q
        return not(q_diff % 2 == 0 and q_diff // 2 * 9 == diff)