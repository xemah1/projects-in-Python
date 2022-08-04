class Solution:
    def firstMissingPositive(self, nums) -> int:
        result = dict()
        for i in nums :
            if i in result.keys() :
                result[i] += 1
            else :
                result[i] = 0
        for i in  range(1,len(nums) + 5) :
            if not (i in result.keys()) :
                return i
        if (nums[0] == 1 and len(nums) == 1) :
            return 2
        else :
            return (nums[0] - 1)

nums = [1,2,3,4,5,67,8,9,6,4,6,7,8,5,3,5,6]
Obj = Solution()
print(Obj.firstMissingPositive(nums))