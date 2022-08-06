class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie
        pigs = 0
        while (t + 1)**pigs < buckets :
            pigs += 1
        return pigs

obj = Solution()
print(obj.poorPigs(956,15,60))