def CountOddNumbers(low,high):
    count = 0
    for i in range(low,high+1):
        if i%2!=0:
            count += 1
    return count
print(CountOddNumbers(3,7))

class Solution(object):
    def countOdds(self,low,high):
        return (high+1) // 2 - low//2
        
