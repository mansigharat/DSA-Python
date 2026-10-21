class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers)-1
        sum = 0
        while start < end:
            sum = numbers[start] + numbers[end] 
            if sum == target:
                return list([numbers[start], numbers[end]])
            elif sum < target :
                start += 1
            elif sum > target:
                end-= 1
        else:
            return 0
    twoSum([2,7,11,15],9)