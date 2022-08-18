class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        k = 0
        while i != len(nums) - 1 :
            if nums[i] == nums[i + 1] :
                k += 1
            if k == 2 :
                nums.remove(nums[i])
                i -= 1
                k -= 1
            if nums[i] != nums[i + 1] :
                k = 0
            i += 1
        return nums.sort()

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,1,2,3,3]))