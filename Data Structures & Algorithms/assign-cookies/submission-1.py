class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i =j = 0

        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                # move to next cookie
                j += 1
            if j == len(s):
                break

            i += 1
            j += 1

        # whereever i is, before that children we are able to satify
        return i
