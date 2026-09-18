def smallerNumbersThanCurrent(nums):
    answer = []
    for i in nums:
        count = 0
        for j in nums:
            if i > j:
                count += 1
        answer.append(count)
    return answer
print(smallerNumbersThanCurrent([8, 1, 1, 2, 3]))

class Solution(object):    
    def smallerNumbersThanCurrent(self,nums):
        sorted_nums = sorted(nums)
        positions = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in positions:
                positions[sorted_nums[i]] = i
        answer = []
        for num in nums:
            answer.append(positions[num])
        return answer