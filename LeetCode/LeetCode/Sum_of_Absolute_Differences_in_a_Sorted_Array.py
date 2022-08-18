class Solution:
    def getSumAbsoluteDifferences(self, nums) :
        n = len(nums)
        sum_below = 0
        sum_total = 0
        for num in nums:
            sum_total += num
        
        res = []
        for i in range(n):
            num = nums[i]
            sum_total -= num
            res.append(sum_total - (n - 1 - i) * num + i * num - sum_below)
            sum_below += num
        return res

obj = Solution()
print(obj.getSumAbsoluteDifferences([1,4,6,8,10]))