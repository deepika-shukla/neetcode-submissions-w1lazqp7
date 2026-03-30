class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res =[]

        def backtrack(open, close):
            if open == close == n:
                # we found one answer
                res.append("".join(stack))
                return
            
            # we can add open any time
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            # we can add close only when open is still there    
            if close < open: 
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
            
        backtrack(0,0)
        return res