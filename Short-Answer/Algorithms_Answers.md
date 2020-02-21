#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

Answer: O(n)
```
Explanation: As the input grows the algorithm takes longer to complete or come to a conclusion. In the this case the input factors in for the loops.
```

b)
Answer: O(nLogn)
```
With the nested loops: J looping half the times due to multipling J by 2 and N times range loop.
```

c)
Answer: O(n)
```
The computational time for completion increases with the size of the input. So input of 4 would have to do 4 recursive calls.
```

## Exercise II

We could have a (n) amount of floors. We can toss egg(s) per (n) floors and see if the egg breaks. If the egg breaks at a floor while trying each floor of (n) floors, then the remainder of the incrementing floors would break the egg. Vice versa for egg(s) not breaking with the floors going lower of (n) floors.

```
PSEDUO CODE:

PARAMETERS: EGG, START=0

RECURSION.

// HAVE 2 BASE

    // IF EGG BREAKS IS TRUE, RETURN FLOOR.

    // IF FLOOR IS 0 OR 1 RETURN FLOOR.

// IF (FLOOR = 100) > START AND EGG !=, CALL RECURSIVELY(EGG,START +1)

// FOR EVERY FLOOR THE EGG WILL EITHER BREAK OR NOT BREAK. (TRUE OR FALSE)

// GET INDEX OF WHERE DROPPED EGG BREAKS AND SLICE THE REMAINDER OF THE FLOORS ABOVE THAT INDEX AS THOSE WILL BREAK THE EGGS.

// RETURN REMAINDER OF START AND EGGS FROM FLOORS THAT ARE DISCOVERED AS BREAKING EGGS
```

Complexity: O(n)
