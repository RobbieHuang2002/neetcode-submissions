class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1 
        return False