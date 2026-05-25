class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we need to check if we are able to break word
        dp = [False] * (len(s)+1)
        # empty string is True
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: # check starting word and complete
                    dp[i] = True
                    break
        return dp[len(s)]