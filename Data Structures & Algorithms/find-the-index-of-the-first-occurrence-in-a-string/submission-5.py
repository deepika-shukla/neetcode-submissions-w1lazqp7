class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        k = 0

        while k < len(haystack):
            if needle[i] == haystack[k]:
                j = 0
                i = k
                ans = ""
                while j < len(needle) and k < len(haystack) and needle[j] == haystack[k]:
                    ans  += needle[j]
                    j += 1
                    k += 1
                if ans == needle:
                    return i
                else:
                    k = i+1
                    i = 0
            else:
                i = 0
                k += 1
                
        return -1

