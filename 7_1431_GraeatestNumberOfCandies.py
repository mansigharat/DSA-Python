def kidsWithCandies(extraCandies , candies):
    return [(i+extraCandies) >= max(candies) for i in candies]
