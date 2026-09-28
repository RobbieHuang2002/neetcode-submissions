class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        final = []

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        for i, n in hashmap.items():
            final.append([n,i])
        final.sort()

        res = []
        while len(res) < k:
            res.append(final.pop()[1])
        return res
