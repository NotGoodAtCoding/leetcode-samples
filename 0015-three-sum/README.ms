This one was tricky. Edge cases really get to you on this one, though the simpler you can make the "fix" the better, as always.

Very much an addendum to two sum ii.

By iterating through the sorted list then selecting the remaining list as the input list for two sum and the inverse of the iterated element, you reduce the problem to two sum with the caveats:

1. the list contains duplicates
2. the answer set must not contain duplicates

We account for this by, in the top level iteration, skipping new candidates for evaluation that match the previous candidate, as well as continuing to skip "start" pointer values that match the previous value when implementing the nested iteration with start/end (left/right) pointers. 
