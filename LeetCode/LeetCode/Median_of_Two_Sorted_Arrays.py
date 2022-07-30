nums1 = [1,3,5,7,9]
nums2 = [2,4,6]

nums = nums1 + nums2
nums.sort()
low,high = (len(nums) - 1) // 2, len(nums) // 2
if (low == high) :
    print(nums[high])
else :
    print(((nums[high] + nums[low]) / 2))