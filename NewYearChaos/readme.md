## Problem
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by *1* from *1* at the front of the line to *n* at the back.  

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if *n = 8* and *Person = 5* bribes *Person = 4*, the queue will look like this: *1, 2, 3, 5, 4, 6, 7, 8*.  

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

## Input
- q: an array of integers

## Output
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print **Too chaotic** if the state is invalid, i.e. it requires a person to have bribed more than *2* people.

## Sample
Input
```
q = [[5, 1, 2, 3, 7, 8, 6, 4], [1, 2, 5, 3, 7, 8, 6, 4]]
```
Output
```
Too chaotic
7
```