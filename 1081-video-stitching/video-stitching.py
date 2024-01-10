class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if not clips:
            return 0
        clips.sort(key=lambda x:(x[0], -x[1]))
        s, e = 0,0
        count = 0
        i = 0
        while i < len(clips):
            if clips[i][0] > e:
                return -1
            maxi = e
            while i < len(clips) and clips[i][0] <= e:
                maxi = max(maxi, clips[i][1])
                i += 1
            count += 1
            e = maxi
            if e >= time:
                return count
        return -1