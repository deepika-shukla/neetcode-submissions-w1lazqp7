class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in d:
                d[tuple(count)].append(s)
            else:
                d[tuple(count)] = [s]
        return list(d.values())
