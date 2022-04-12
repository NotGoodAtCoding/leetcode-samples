def partitionLabels(s: str) -> List[int]:
    partitions = []
    rev_str = s[::-1]
    partition_start = partition_end = -1
    seen = set()
    for idx, char in enumerate(s):
        if char not in seen:
            partition_end = max(partition_end, (len(s)-1) - rev_str.index(char))
        seen.add(char)
        if idx == partition_end:
            partitions.append(partition_end - partition_start)
            partition_start = partition_end
            seen = set()

    return partitions
