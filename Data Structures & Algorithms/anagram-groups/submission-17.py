class Solution:
    # how can i improve?
    # def order(self, s):
    #     o = 0
    #     for i in s:
    #         o += ord(i) - ord("a") + 99999
    #     return o
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     dict_of_anagram = {}

    #     for s in strs:
    #         o = self.order(s)
    #         if o not in dict_of_anagram:
    #             dict_of_anagram[o] = []
    #         dict_of_anagram[o].append(s)
    #     return list(dict_of_anagram.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in d:
                d[tuple(count)] = []
            d[tuple(count)].append(s)
        return list(d.values())
            
                

        