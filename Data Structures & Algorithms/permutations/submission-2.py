class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            next_permutations = []
            for p in permutations:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    next_permutations.append(p_copy)
            permutations = next_permutations
        return permutations
