class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ##########3 backtrack !!!!!!!!!!11
        # res = []
        # cur = []

        # def backtrack(i):
        #     if i == len(s):
        #         res.append(" ".join(cur))
        #         return

        #     for j in range(i, len(s)):
        #         w = s[i:j+1]
        #         if w in wordDict:
        #             cur.append(w)
        #             backtrack(j+1)
        #             cur.pop()


        # backtrack(0)
        # return res


        ############ CACHE ############
        wordDict = set(wordDict)
        cache = {}
        def backtrack(i):
            # in this solution we are hadnling the edge case
            # by returning empty string
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
            
            # and we are forming sentences now
            # if we are not able to form then empty list res will be returned
            res = []
            for j in range(i, len(s)):
                w = s[i:j+1]
                # if w does not exist move to next
                if w not in wordDict:
                    continue
                
                strings = backtrack(j+1) # you will get list of string
                for substring in strings:
                    sentence = w
                    # if substring is empty we does not need to add
                    # in our possible sentence
                    if substring:
                        sentence += " " + substring
                    res.append(sentence)
            cache[i] = res
            return res
        
        return backtrack(0)
