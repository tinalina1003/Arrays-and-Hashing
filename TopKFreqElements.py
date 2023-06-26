# Given an integer array nums and an integer k, return k most frequent elements. You may return the answer in any order

# use algorith called Bucket Sort: linear time (bounded only)

# make a list of count instead and map it to a list of numbers that have exactly that many count
# bounded by size of list so if all values are the same, then at max it can be is the max number of count

# use hash map again

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} #create hash map
        freq = [[] for i in range(len(nums) + 1)] #list of lists (this is because max it can be is the max size of the list)
        for n in nums:
            count[n] = 1 + count.get(n, 0) # returns 0 if the value doesn't exist, typical of .get() function in a hashmap
        for n, c in count.items(): #returns key,value pair in the dictionary
            freq[c].append(n) # count(number of times it occurs) is the index and append value n to the list for that count

        res = [] #this is the empty list to keep track of the top k most frequent elements

        for i in range(len(freq) - 1, 0, - 1): # range(size, end, increments)
            for n in freq[i]:
                res.append(n) # this will create a list of the top k elements
                if len(res) == k: # we know at max length is k so if len(res) matches k, then just return the list of results
                    return res
                
list1 = [1, 1, 1, 2, 2, 100, 100]

s = Solution()

outputRes = s.topKFrequent(list1, 2)

print(outputRes)