#Given a list of non-negative integers, arrange them such that they form the largest number.
#asked in delloite 2 round of interview
Example:

Input: [3,30,34,5,9]

Output: "9534330

li = ['3','30','34','5','9']
import itertools as it
combinations = it.permutations(li)
a=["".join(i) for i in combinations]
print(max(a))
    
