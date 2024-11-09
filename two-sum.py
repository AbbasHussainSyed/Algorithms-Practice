class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """# brutefore approach:
        for i in range(len(nums)-1) :
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:      
                    return [i,j]"""

        #using hashmap dictionary
        numToIndexMap = {}
        diff = []
        for index, num in enumerate(nums):
            if diff == target - num:
                if diff in numToIndexMap:
                    return [index, numToIndexMap[diff]]
        return "null"

nums = [2, 7, 11, 15]
target = 13

solution = Solution()

result = solution.twoSum(nums, target);
print(result)