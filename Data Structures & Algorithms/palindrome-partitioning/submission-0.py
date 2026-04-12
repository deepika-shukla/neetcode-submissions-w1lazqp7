class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #edge cases: single character is pallindrome
        # empty string is pallindrome
        # we can subdivide the problem

        res =[]
        par = []

        def dfs(i):
            # if we reach the last of index, that means
            # we found the pallindrom partition
            if i >= len(s):
                res.append(par.copy())
                return
            
            # now we need the division
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    par.append(s[i:j+1])
                    dfs(j+1)
                    par.pop() # backtrack
        
        dfs(0)
        return res
    
    def isPali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


