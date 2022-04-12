Conceptually, this problem was very simple. Most of the pain came from interacting with the data structure, which I suppose was the point of the exercise.

The math portion is similar to an adder circuit but with base10 - store the value, send the carry to the next iteration.

Quick Visualization:

```
input: l1= [2,4,3] l2 = [5,6,4]

iter 0:
carry = 0
node1 = { val:2 }
node2 = { val:5 }

new_digit = first = last = ListNode(val=7)

iter1:
carry = 0
node1 = { val:4 }
node2 = { val:6 }

new_digit = last = ListNode(val=0)
first = ListNode(
  val=7,
  next=ListNode(val=0)
)

iter2:
carry = 1
node1 = { val:3 }
node2 = { val:4 }

new_digit = last = ListNode(val=8)
first = ListNode(
  val=7,
  next=ListNode(
    val=0,
    next=ListNode(
      val=8
      )
    )
  )
```
