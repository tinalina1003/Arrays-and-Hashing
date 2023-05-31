# Given an array of strings str, group the anagrams together. You can return the answers in any order

# Example 1: strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Output  =  [['bat'], ['nat', tan], ['ate', 'eat', 'tea']]

import collections

class solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list) # mapping charCount to list of anagrams
        
        for s in strs:
            count = [0] * 26 # creates an empty list of length 26 with values of 0

            for c in s: # for each letter in the string provided in the list
                count[ord(c)-ord('a')] += 1 # ord() converts a character to its corresponding Unicode code point, which is useful for performing operations such as indexing or arithmetic on characters.

            ans[tuple(count)].append(s)
            """
                tuple(count): Converts the count list, which contains the count of characters, into a tuple. Tuples are used as keys in the ans dictionary because lists are not hashable and cannot be used as dictionary keys.

                 ans[tuple(count)]: Accesses the value associated with the key tuple(count) in the ans dictionary. If the key does not exist in the dictionary, defaultdict will automatically create a new list as the default value for that key.

                .append(s): Appends the string s to the list associated with the key tuple(count) in the ans dictionary. This ensures that anagrams with the same character count are grouped together in the dictionary.
            """
        return ans.values()
    
strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

s = solution()

results = s.groupAnagrams(strs)

print(results)
