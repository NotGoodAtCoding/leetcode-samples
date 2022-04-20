Naive solution is to keep a sorted list of all the elements, then return the kth item (assuming it's reverse order).
But we notice that we don't actually care about keeping track of any elements smaller than the kth at any point in time, so we can limit the size of the list we sort to k, insert into the list with binary insert and limit it to the top k elements.
This was my second naive solution, though it should have insertion time of O(logn) which should be similar to insert into heap. I suspect that since heap is much better on the average case, this accounts for the performance difference.

The heap implementation is simple and performant. Keep a max heap of size k, insert and cull the heap as needed, and the 0th element is the kth largest. More details in code comments. 
