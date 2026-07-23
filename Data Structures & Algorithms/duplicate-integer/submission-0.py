class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #store data first 
        sets = set()
        for num in nums:
            if num in sets:
                return True
            sets.add(num)
        return False

        

        