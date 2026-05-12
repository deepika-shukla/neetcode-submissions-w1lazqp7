class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}
        # keep the character with index
        for i,c in enumerate(order):
            index[c] = i
        
        for i in range(len(words)- 1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                #compare the different characters
                if w1[j] != w2[j]:
                    # now check the order
                    if index[w2[j]] < index[w1[j]]:
                        return False
                    break
        return True