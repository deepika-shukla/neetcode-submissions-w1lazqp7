class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0 
        for word in words:
            w = 0
            found = True
            while w < len(pref) and w < len(word):
                if pref[w] != word[w]:
                    found = False
                    break
                w += 1
            if found:
                count += 1
        return count
                    