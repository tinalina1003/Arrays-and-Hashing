# Given 2 strings s and t, return true if t is an anagram of s, and false otherwise

class solution:
    def anagram(self, s: str, t: str) -> bool: # using ":" tells python the type that each paramter takes
        #return sorted(s) == sorted(t)
    
        #return Counter(s) == Counter(t) 

        if len(s) != len(t): #if the lengths aren't even the same, then obviously they can't be anagrams
            return False
        countS, countT = {}, {} #this creates an empty dictionary

        # buiild hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # countS[s[i]] selects the letter of the word as the key; the = is the value to the key.  .get() retrieves the value associated with a given key. Second argument sets default value if specified key not found
            # in this case, if value to s[i] doesn't exist, then value = 0, if value exists, +1 to current value
            # countS[s[i]] is the key... countS[key] in this case it's letter s[i].. this line basically updates the key's value to 1 + countS.get() IF it exists... if not, then set it to 0
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #iterate through hashmap
        for c in countS:
            # this means if key doesn't exist by comparing countS and countT. using .get() will stop it from giving us a key error.. 
            # using .get() here ensures that there is a value to compare to if c doesn't exist in countT since we were counting the values in countS
            if countS[c] != countT.get(c, 0):
                return False
            
        return True

word1 = "anagram"

word2 = "naaragm"

Rsolution = solution()

result =  Rsolution.anagram(word1, word2)

print(result)