It seemed straightforward to assume the the order that the dishes should be prepared in would always be in ascending order of satisfaction. Probably easy to prove as well, but I trusted intuition for the sake of time.

Given that (correct) assumption and the fact that all dishes should be prepared if they all have positive satisfaction, the question becomes: Should we add a dish with negative satisfaction to the menu / courses?

What happens when we add a dish to the courses? We change the value of `satisfaction` by the value `last_satisfaction + current_dish_satisfaction` and we obviously don't want to do this if that value is less than 0.

## Code Walkthrough

```
def maxSatisfaction(self, satisfaction: List[int]) -> int:
    # sort is needed as explained above
    satisfaction.sort(reverse=True)

    # init some vars.
    # last tracks the last iteration's satisfaction value
    # current tracks the value of adding the current iteration's dish
    # su (sum) tracks the sum of satisfaction
    last = current = su = 0

    for dish in satisfaction:
        current = last + dish
        if current < 0:
            # don't add a dish that adds negative value
            break
        su += current  # current "course" value is added
        last += dish   # last course with the new dish added

    return su
```

You may think "Well, current isn't needed, you can just use `last + dish` in those two places instead." But this makes execution 9ms slower so it stays. Could be variance...

## Naive approach
Originally it seemed like an ok application of recursion, by first sorting the list is reverse order then comparing the value of the proposed dish add to the value of the recursively determined satisfaction of the list of dishes excluding the proposed one, but that was overcomplicated and non-performant. The value of adding a dish and the calculated new value can be determined from just the previous value and the proposed dish.  
