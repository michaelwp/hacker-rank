## Problem
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica wants to spend as much as possible for the *2* items, given her budget.  
Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.  
For example, suppose she has *b = 60* to spend. Three types of keyboards cost *keyboards = [40, 50, 60]*. Two USB drives cost *drives = [5, 8, 12]*. She could purchase a *40 keyboard + 12 USB drive = 52*, or a *50 Keyboard + 8 USB drive = 58*. She chooses the latter. She can't buy more than *2* items so she can't spend exactly *60*.

## Input
- keyboards: an array of integers representing keyboard prices
- drives: an array of integers representing drive prices
- b: the units of currency in Monica's budget

## Output
Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.


## Sample Input 1
```
b = 10
keyboards = [3, 1]
drives = [5, 2, 8]
```
## Sample Output 1
```
9
```
## Explanation
She can buy the *2nd = 1* keyboard and the *3rd = 8* USB drive for a total cost of *1 + 8 = 9*.

## Sample Input 2
```
b = 5
keyboard = 4
drive = 5
```
## Sample Output 2
```
-1
```
## Explanation
There is no way to buy one keyboard and one USB drive because total price *drives + keyboards > b (5 + 4 = 9) > 5*, so we print *-1* .