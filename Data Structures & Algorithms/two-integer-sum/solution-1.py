class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            pos = []
            t = target-v
            if t in nums and nums.index(t)!=i:
                pos_start = i
                pos_end = nums.index(t)
                pos.extend([pos_start,pos_end])
                pos.sort()
                return pos
                break
