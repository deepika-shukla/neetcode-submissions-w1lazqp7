class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maxf even if we reduce the count when shrinking window, its okay to keep maxf same, as our result will only chnage when maxf is increased then only we will find new longest string.

        l = 0
        maxf = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            maxf = max(maxf, count[s[r]])

            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res