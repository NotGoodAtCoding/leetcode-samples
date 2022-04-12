It's just binary search with a few extra steps / considerations. I thought about this for too long thinking that there could be edge cases that this algorithm does not account for but it turns out to be fine. Reduce the problem until you eliminate the pivot from the space and you are good to go.

Also ignore the runtime on leetcode, it is too inconsistent to really mean anything. This algorithm is theoretically log(n), but just returning `contains(target)` usually performs about as well and sometimes better. 
