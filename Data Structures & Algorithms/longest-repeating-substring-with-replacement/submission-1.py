class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #store the maximum frequency of character
        maxf = 0

        #to maintain the window size
        l = 0

        #maintain the count of characters
        count = {}

        #now start from the beggining
        for r in range(len(s)):
            # increase count of character
            count[s[r]] = 1 + count.get(s[r], 0)

            #update maxf if any othe maximum found
            maxf = max(maxf, count[s[r]])

            # check if swaps are available, if it increased
            # move the l, and decrese the count of character at l index
            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l +=1 
        
        # return teh size of window
        return (r-l+1)

        