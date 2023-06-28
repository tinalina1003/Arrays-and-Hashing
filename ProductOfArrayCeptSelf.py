""" Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i]

 the product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

you must write an algorith that runs O(n) time and without using division operation


 example:

 input: nums = [1, 2, 3, 4]
 output: [24, 12, 8, 6]

 input: nums = [-1, 1, 0, -3, 3]
 output: [0, 0, 9, 0, 0]

 we'll compute prefix positions (from beginning) and postfix positions (from end). This is element INCLUSIVE meaning you will need to multiply the current numbered element by
 by the numbers before/after it as well

 pre/post fix means that if I am finding the 3rd position of the output, I will multiply the first and second elements in the prefix array and multiply that by the fourth
 and third postfix elements to get our output

 example:

 prefix = [1, 2, 6, 24], our first element would need a default 1 prefix before so 1x1 is 1 which would be filled in the first element
 second element would have 1x2 (because 2 is the current and you multiply by the one before it)
 third element is 1x2x3
 fourth element is 1x2x3x4

 postfix = [24, 24, 12, 4]
 first element is 4x3x2x1
 second element is 4x3x2
 third element is 4x3
 fourth element is 4x1 (postfix default with 1 as a number prior)

 instead of creating 2 lists, we will create 1 output, fill it with prefix then apply postfix operation to get final solution

 Output values are the i-1th element of prefix and multiply by i+1 element of postfix
 ex) first element is 0th element defaulted as 1 x 2nd element 24 = 24
 second element is 1st element of prefix 1 multiplied by 3rd element of postfix 12 = 12
 third element would be 2x4
 fourth element is 6x1 (postfix 5th element default as 1)
 """

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len((nums))) # creates a list with len nums with all values of 1

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # update prefix with current prefix and multiply by current nums value [1, 2, 6, 24]: 1x1, 1x2, 2x3, 6x4
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # range(start, stop, step) starts at 3, ends at -1 (print values are 3, 2, 1, 0)
            res[i] *= postfix # multiply the current res value with postfix and update
            postfix *= nums[i]
        return res

s = Solution()

output = s.productExceptSelf([1, 2, 3, 4])

print(output)