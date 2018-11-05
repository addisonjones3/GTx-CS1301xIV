# !/usr/bin/env python

# Write a function called are_anagrams. The function should
# have two parameters, a pair of strings. The function should
# return True if the strings are anagrams of one another,
# False if they are not.
# 
# Two strings are considered anagrams if they have only the
# same letters, as well as the same count of each letter. For
# this problem, you should ignore spaces and capitalization.
# 
# So, for us: "Elvis" and "Lives" would be considered
# anagrams. So would "Eleven plus two" and "Twelve plus one".
# 
# Note that if one string can be made only out of the letters
# of another, but with duplicates, we do NOT consider them
# anagrams. For example, "Elvis" and "Live Viles" would not
# be anagrams.


# Write your function here!
def are_anagrams(word1, word2):
    word1members = {}
    word2members = {}

    is_anagram = True

    for letter in word1:
        if not letter.isalpha():
            continue
        if letter.lower() not in word1members:
            word1members[letter.lower()] = 1
        else:
            word1members[letter.lower()] += 1
    
    for letter in word2:
        if letter == ' ':
            continue
        if letter.lower() not in word2members:
            word2members[letter.lower()] = 1
        else:
            word2members[letter.lower()] += 1

    print word1members
    print word2members

    if len(word1members) == len(word2members):
        for member in word1members.keys():
            if member in word2members.keys() and word1members[member] == word2members[member]:
                        continue
            else:
                is_anagram = False
                break
    else:
        is_anagram = False

    return is_anagram



# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
# 
# If your function works correctly, this will originally
# print: True, False, True, False, each on their own line.
print(are_anagrams("New Calculus", "Precalculus"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))
