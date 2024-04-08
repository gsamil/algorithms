There were 2 questionf from coderbyte

- 1st one is [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/) from leetcode.

- 2nd one is Minimum Distance, not sure where it's from. I coulnd't solve it because I didn't understand the question for a long time.

# Minimum Distance

Terra is looking to maximize everyone's deep work by giving everyone a room numbered 1 to N connected by one way paths going from 1 to N. (i.e. you now have paths going from (1 -> 2 -> 3 -> 4 -> 5 -> ... -> N))

The layout at the moment is not very efficient and we want to build new paths:

These paths are constructed in a way such that:

- They are one way paths that can go from any point a = [1..N] to any point b = [1..N] such that a is always less than b (a < b)
- They will not intersect. Meaning, if we have 2 roads A -> B and C -> D, then there will be no case such that A < C < B < D
- There will be no repeated paths

You are given two lists denoted as A and B, and an integer N. 'A' will denote the starting points of the new paths being built, and 'B' will denote the end points of the new paths. (i.e. for a given path A[k] will lead to B[k]). Find the distance of the shortest path a terra-rian starting at room 1 can go to room N for every new road built. Then return the sum of all these shortest paths.

### Assume:

- Any values in A or B will be less than or equal to N
- For any new path A[k] and B[k] -> A[k] < B[k]
- List A and B both have the same length

### The input:

You will receive a list of values interpreted as:

- First element -> Number of new paths that will be built
- Starting points of the new paths [List A]
- End point of the new paths [List B]
- N

## Example 1

Input: [2, 1, 4, 3, 6, 8]

A = [1, 4] B = [3, 6] N = 8, The shortest path when path 1 -> 3 is built, is 1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8. Hence the distance is 6.

The shortest path when road 4 -> 6 is build is 1 -> 3 -> 4 -> 6 -> 7 -> 8 with distance 5.

Hence you return sum of [6, 5] = 11

## Example 2

Input: [2, 1, 1, 8, 4, 8]

A = [1, 1] B = [8, 4] N = 8, The shortest path when path 1 -> 8 is built, is 1 -> 8. Hence the distance is 1.

Any new path built does not improve the distance, hence you return sum of [1, 1] = 2

