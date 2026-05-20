class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # A set to keep track of elements that have been seen
        seen = set()
        # A list to store duplicates found in the input list
        # duplicates =#  []

        # Iterate over each element in the list
        for i in nums:
            if i in seen:
                
                return True
            seen.add(i)
        return False


            