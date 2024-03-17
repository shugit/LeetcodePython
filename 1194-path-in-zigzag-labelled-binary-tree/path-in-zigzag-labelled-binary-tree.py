class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 0
        level_max = 1
        level_min = 1
        cnt = 1
        while level_max < label:
            level += 1
            cnt = cnt * 2
            level_min, level_max = level_max + 1, level_max + cnt
        path = []
        while label >= 1:
            path.append(label)
            level_max = pow(2, level + 1) -1
            level_min = pow(2, level)
            label = (level_max + level_min - label) // 2
            level -= 1
        return path[::-1]
            