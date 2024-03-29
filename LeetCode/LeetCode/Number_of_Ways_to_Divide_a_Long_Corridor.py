class Solution:
    def numberOfWays(self, corridor: str) -> int:
        numSeats = 0
        numPlants = 0
        dividers = 1
        
        for i in corridor :
            if i == 'S':
                numSeats += 1
            if numSeats == 2 and i == 'P':
                numPlants += 1
            if numSeats == 3 :
                dividers *= (numPlants + 1)
                dividers  %= 1000000007
                numSeats = 1
                numPlants = 0
        
        if numSeats < 2 : 
            return 0
        return dividers

s = "SSPPSPS"
Obj = Solution()
print(Obj.numberOfWays(s))