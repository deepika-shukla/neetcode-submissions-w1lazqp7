class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we need backtracking in this therefore we will use Stack
        stack = []

        for a in asteroids:
            
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                # - wala bada hai
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    # make it zero we don't want
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
                 
        return stack
