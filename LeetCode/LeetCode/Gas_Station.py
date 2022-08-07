class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n, total_gassu, gassu, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_gassu += gas[i] - cost[i]
            gassu += gas[i] - cost[i]
            if gassu < 0:
                gassu = 0
                start = i + 1
        return -1 if (total_gassu < 0) else start

obj = Solution()
print(obj.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))