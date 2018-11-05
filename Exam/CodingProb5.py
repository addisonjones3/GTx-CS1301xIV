# !/usr/bin/env python

# Write a function called count_capital_consonants. This
# function should take as input a string, and return as output
# a single integer. The number the function returns should be
# the count of characters from the string that were capital
# consonants. For this problem, consider Y a consonant.
# 
# For example:
# 
#  count_capital_consonants("Georgia Tech") -> 2
#  count_capital_consonants("GEORGIA TECH") -> 6
#  count_capital_consonants("gEOrgIA tEch") -> 0


# Write your function here!
def count_capital_consonants(instring):
    vowels = ['a', 'e', 'i', 'o', 'u']
    uppercons = 0
    for letter in instring:
        if letter.lower() not in vowels and letter.isupper():
            uppercons += 1
    return uppercons


# The lines below will test your code. Feel free to modify
# them. If your code is working properly, these will print
# the same output as shown above in the examples.
print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))


