import heapq

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        result = [val for row in matrix for val in row]
        heapq.heapify(result)
        for i in range(k):
            ans = heapq.heappop(result)
        return ans

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
obj = Solution()
print(obj.kthSmallest(matrix,k))