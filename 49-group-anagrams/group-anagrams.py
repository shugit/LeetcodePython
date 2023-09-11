class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            k = sorted(s)
            key = "".join(k)
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]
        return m.values()
            