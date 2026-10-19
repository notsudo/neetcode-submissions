class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        needs = set()

        for j in nums:
            if j in needs:
                return True
            else:
                needs.add(j)
        return False       