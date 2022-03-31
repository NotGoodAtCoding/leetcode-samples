When trying to solve this problem, I had an implementation of path traversal which didn't properly detect what the duplicate was after detecting the cycle in the graph so once I hit my time limit I went with the boring add and check map:
```
# linear add space, linear time
exists = {}
for n in nums:
    if exists.get(n):
        return n
    exists[n] = True
return -1
```
Which does not fulfill the problem requirements.

We notice that since the elements of the list are all integers with values under `len(nums)` and that by using a value-index traversal we can at least detect that there exists a cycle when we use two indexes to get the same value, we need to find a way to detect when that would happen. So, I had an "ahead" and "behind" traversal, one that would traverse twice per iteration and the other just once, knowing that they would eventually meet and I would know we are in the cycle at that point, but I had no idea how to move on from there.

## Actual Solution
The proper algorithm does start with path traversal, but then uses Floyd's algorithm for detecting the beginning of a cycle. I had never heard of this algorithm before, so this was a good learning experience.

We start by setting our fast and slow runners, then we let them go using index-value traversal with the "fast" runner going twice the "speed" by covering two index-value jumps while the slow goes to just one. Once they meet, we know we have entered the cycle.

```
fast = slow = nums[0]
while True:
    fast = nums[nums[fast]]
    slow = nums[slow]

    if fast == slow:
        break
```
We see this run on an example list, f is fast, s is slow runner:
```
 fs
[1, 3, 4, 2, 2]

    s        f
[1, 3, 4, 2, 2]

             fs
[1, 3, 4, 2, 2]
```

As an aside: what tripped me up here was thinking that the "runners" could miss each other, by the faster one leapfrogging but that's quickly disproven by a quick induction: if they are the same, we exit. if slow is one ahead of fast, next they will be the same, if slow is two ahead of fast, next they will be only one ahead, etc.

So, we now know that the two runners have entered the cycle, but what we do not know is whether they are at the duplicate or not. That's where we reset "fast," make them iterate at the same rate, and then let them intersect again:

```
fast = nums[0]

while fast != slow:
    fast = nums[fast]
    slow = nums[slow]
```
Which we see play out with our example:

```
             fs
[1, 3, 4, 2, 2] # previous state

 f           s
[1, 3, 4, 2, 2] # set fast to nums[0]

    f  s
[1, 3, 4, 2, 2]

             fs
[1, 3, 4, 2, 2]
```

The reason this algorithm works is that the distance (number of iterations) between where the slow and fast runners intersect and the start of the cycle and the start of the iteration to the start of the cycle will always be equal. This works out more algebraically than I would reasonably expect to be able to reason about in a coding interview.

```
The fast runner iterates twice for every time the slow runner iterates;
  2 * slow = fast

In order to get to the intersection, both will cover a distance of:
  ( initial path to get into the cycle ) + ( length of the cycle ) - ( distance from start of cycle to intersection )
  denoted as ( i + c - d )

However, the fast runner may traverse the cycle any number of times while "waiting" for the slow runner to catch up, but we can ignore this distance via modulo since we really only care about the distance from when the slow runner enters the cycle, which since the slow runner must traverse the distance c, we know the fast runner traverses 2c in that number of iterations.

So, we are left with

  2 (slow) = fast

  2 (i + c - d) = i + 2c - d
  2i + 2c -2d   = i + 2c - d
  i - d         = 0

  i = d
  initial path = distance from intersection to start of cycle
```

I did not really like this problem, I really thought that this was more of a tricky discrete mathematics quirk than any kind of actual coding ability question :/ Would I ever come up with the proper solution on my own? No, and certainly not in a coding interview. Would I approve this clever solution in a Code Review? Also probably no, it's very obtuse AND I would likely never actually care about adding a linear amount of memory in an algorithm like this. All that being said, the algorithm and proof were fun to learn about, I would just never give this problem to a candidate I was interviewing. 
