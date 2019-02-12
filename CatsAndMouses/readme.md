## Problem
Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.  
You are given *q* queries in the  form of *x*, *y*, and *z* representing the respective positions for cats *A* and *B*, and for mouse *C*.  

- If cat *A* catches the mouse first, print **Cat A**.
- If cat *B* catches the mouse first, print **Cat B**.
- If both cats reach the mouse at the same time, print **Mouse C** as the two cats fight and mouse escapes.

For example, cat *A* is at position *x = 2* and cat *B* is at *y = 5*. If mouse *C* is at position *z = 4*, it is *2*  units from cat *A* and *1* unit from cat *B*. Cat *B* will catch the mouse.

## Input
- x: an integer, Cat A's position
- y: an integer, Cat B's position
- z: an integer, Mouse C's position

## Output
For each query, return Cat A if cat *A* catches the mouse first, Cat B if cat *B* catches the mouse first, or Mouse C if the mouse escapes.

## Sample 1
```
x, y, z = [1, 2, 3]
```
## Output
```
Cat B
```
## Explanation
```
[ Cat A ] -> [ Cat B ] -> [ Mouse C ]
[   1   ] -> [   2   ] -> [    3    ]

Cat B is Closest to Mouse C, so Cat B will catch the Mouse C
```

## Sample 2
```
x, y, z = [1, 3, 2]
```
## Output
```
Mouse C
```
## Explanation
```
[ Cat A ] -> [ Mouse C ] -> [ Cat B ]
[   1   ] -> [    2    ] -> [   3   ]

Both Cat A and Cat B is close to the Mouse C, so they will fight to over the Mouse C, then the Mouse C will escape.
```