## Problem
> We define a single roll operation on a string to be the circular increment of each character by one. In other words, each character is rolled forward and overwritten with the next alphabetic character. Looking at the English alphabet, characters in the range ascii[a-z], a becomes b, b becomes c, and z becomes a.
> Given an array of integers named roll, we want to perform a roll operation on the first roll[i] characters of s for each element i in the array. Given a zero indexed string, an operation roll[i] affects characters at positions 0 through (roll[i]-1).

> For example, if string s = abz and roll = [3, 2, 1], we perform the following sequence of operations:
- roll[0] = 3: Roll all three characters so abz becomes bca.
- roll[1] = 2: Roll the first two characters so bca becomes cda.
- roll[2] = 1: Roll the first character so cda becomes dda.
> After performing all the operations, the final value of s is dda.