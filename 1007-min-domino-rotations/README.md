We start with a set of valid "solutions" - that is, values that the dominoes can be flipped to in order for either the tops or bottoms to be all matching - equal to the value of the top and bottom of the first domino. We then take the intersection of these valid solutions with the values of the top and bottoms of all the dominoes. If any domino is missing a value, then that's no longer a vlid solution and the dominoes must all be flipped to the other value. If we run out of valid solutions, then we return -1 indicating no solution.

Once we determine the space of valid solutions, we can determine the minimum flips to reach one of these endpoints. I practically brute-forced this solution by checking how many flips it would take to make the top or bottom match each solution, take the min of those values, then the min of those two against each other.

I tried optimizing this by tracking flips during iteration, counting the occurrences of each solution in the top and bottom rows during the single iteration, but this did not perform significantly faster than the initial "brute force" method to determine flips required. 

```
def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    valid = {tops[0], bottoms[0]}
    top_sols = {tops[0]: 0}
    bot_sols = {bottoms[0]: 0}

    for top, bottom in zip(tops, bottoms):
        valid = valid.intersection({top, bottom})
        if not valid:
            return -1

        if top == bottom:
            continue
        if top in valid:
            top_sols[top] = top_sols.get(top, 0) +1
        if bottom in valid:
            bot_sols[bottom] = bot_sols.get(bottom, 0) +1

    top_flips = bot_flips = len(tops)
    for solution in valid:
        top_flips = min(top_flips, top_sols[solution])
        bot_flips = min(bot_flips, bot_sols[solution])

    return min(top_flips, bot_flips)
  ```
