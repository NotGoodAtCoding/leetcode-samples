https://leetcode.com/problems/partition-labels/

We notice that a partition is determined by the following reasoning:

1. start a partition by finding the last occurrence of the first char of the partition
2. for each char in the partition (between start and end), further expand the partition if the last occurrence of any of the chars in the partition exceeds the limit of the initially set partition end
3. if (2) expands the partition, be sure to verify the newly contained chars in the partition

So we implement the algorithm like this:

```
def partitionLabels(self, s: str) -> List[int]:
    partitions = []
    rev_str = s[::-1]
    partition_start = partition_end = -1  // initialize to -1 to account for first partition size being one greater than how we calculate later partition sizes.
    for idx, char in enumerate(s):
        // update partition end to be the last occurrence of the given char.
        // common way to get last occurrence is with
        // (len(s)-1) - STRING[::-1].index(char)
        partition_end = max(partition_end, (len(s)-1) - rev_str.index(char))

        // exhausted partition
        if idx == partition_end:
            partitions.append(partition_end - partition_start)
            partition_start = partition_end

    return partitions
```

So we have a working solution, but it's not very efficient since we have a fairly stable O(n^2) runtime due to running index() in every iteration. We notice that we don't need to update the end of the partition if we've already updated it in response to the same char.

So we add a "seen char" set to improve the average case time, though the upper limit is still O(n^2).

```
def partitionLabels(self, s: str) -> List[int]:
    partitions = []
    rev_str = s[::-1]
    partition_start = partition_end = -1
    seen = set()  // minor optimization
    for idx, char in enumerate(s):
        if char not in seen:
            partition_end = max(partition_end, (len(s)-1) - rev_str.index(char))
        seen.add(char)
        if idx == partition_end:
            partitions.append(partition_end - partition_start)
            partition_start = partition_end
            seen = set()

    return partitions
```

I think that this could be further optimized by leveraging sets further, but I have this exercise time-boxed to 30 minutes since I am tired. 
