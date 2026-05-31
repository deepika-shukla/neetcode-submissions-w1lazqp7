class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # recursive
        # def backtrack(i,j):
        #     # edge case
        #     # if we reach at last index of word1 all words of word2 needs to be inserted
        #     if i == len(word1): 
        #         return len(word2) - j
        #     if j == len(word2): # all words of word1 needs to be deleted
        #         return len(word1) - i
            
        #     if word1[i] == word2[j]:
        #         return backtrack(i+1,j+1)
            
        #     else:
        #         # three conditions : insert, delete, replace
        #         return 1 + min(backtrack(i, j+1), backtrack(i+1,j), backtrack(i+1,j+1))
        # return backtrack(0,0)
        
        # Memoization
        dp = {} # indices : operation
        def backtrack(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            # edge case
            # if we reach at last index of word1 all words of word2 needs to be inserted
            if i == len(word1): 
                return len(word2) - j
            if j == len(word2): # all words of word1 needs to be deleted
                return len(word1) - i
            
            if word1[i] == word2[j]:
                dp[(i,j)] =  backtrack(i+1,j+1)
            
            else:
                # three conditions : insert, delete, replace
                dp[(i,j)] = 1 + min(backtrack(i, j+1), backtrack(i+1,j), backtrack(i+1,j+1))
            return dp[(i,j)]
        return backtrack(0,0)