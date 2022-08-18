class Solution:
    def minSetSize(self, arr) -> int:
        dic = dict()
        length = len(arr)
        for i in arr :
            if i in dic.keys() :
                dic[i] += 1
            else :
                dic[i] = 1
        result = list(dic.values())
        result.sort(reverse = True)
        a = 0
        while len(arr) / 2 < length :
            length -= result[0]
            result.remove(result[0])
            a += 1
        return a
        
obj = Solution()
print(obj.minSetSize([3,3,3,3,5,5,5,2,2,7]))