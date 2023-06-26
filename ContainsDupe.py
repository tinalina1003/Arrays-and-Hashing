# given  an interger of arrays nums, return true if any value appears at least twice in the array and return false if every element is distinct


class solutions:
    def containsDupe(self, nums: list[int]) -> bool: # this creates the method's parameters, it is expecting nums which is a li st of integers and returns boolean True or False
        hashset = set() # this creates the set for things the list will compare it to; we use set/list here because in the other example, those are strings

        for n in nums:
            if n in hashset: # this is only used for booleans, cannot check for index unless you use .index()
                return True
            hashset.add(n)
        return False
    
list1 = [1, 2, 3, 1]

s = solutions() # I need to execute the function to access things inside

result = s.containsDupe(list1)

print(result)


