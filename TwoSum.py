# given an array of integers, return indices of the two numbers such that they add up to a specific target

# you may assume that each input would have exactly one solution and you may not use the same element twice

class solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val:index

        for i, n in enumerate(nums):
            diff = target - n # if the difference between target and current number is in in hashmap, then return the pair of val:index
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i # if it's not in the hashmap, then update the hashmap with n, which is the number as a key, and i, the index, as it's value
        return
        
s = solution()

result = s.twoSum([2, 7, 11, 15], 9)

print(result)