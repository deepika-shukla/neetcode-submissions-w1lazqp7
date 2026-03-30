class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # here we need to check for each part of string could we found in 
        #dictionary

        #we will keep track using dp list
        dp = [False]*(len(s)+1)
        #edge condition if we could reach last means we found word
        dp[len(s)] = True

        # we will start from last
        for i in range(len(s)-1,-1,-1):
            #compare for each word
            for w in wordDict:
                #check if we have enough no of letters to compare
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    #we found the word
                    break
        
        # dp[0] will have True or false if we were able to split
        return dp[0]