class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(nums):
            x = nums[i]
            for j in range(i,nums):
                y = nums[j]
                if x+y==target:
                    result = [x,y]

        return result
    
# Better approach
class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash: 
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i