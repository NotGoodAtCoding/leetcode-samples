TODO: Extend explanation

```
def twoCitySchedCost(costs: List[List[int]]) -> int:
    # get diff for each flight and set that as the bias
    # sort by bias and split in half
    # sum costs of flight A from first half, flight b from second half

    biases = [(l[0], l[1], l[0]-l[1]) for l in costs]
    biases = sorted(biases, key=lambda x: x[2])

    total = sum(c[0] for c in biases[:(len(biases))//2]) # first half takes flight a
    total += sum(c[1] for c in biases[(len(biases))//2:]) # second half takes flight b

    return total
```
