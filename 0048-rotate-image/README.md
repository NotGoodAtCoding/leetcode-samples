Yay, linear algebra! Well, not really.
We could implement a rotation via matrix multiplication using the 90* clockwise rotation matrix:

```
[ 0  1]
[-1  0]
```
But this is impossible to do with in-place memory, we would need to create a resultant matrix to store the subtotals or shortcut the multiplication by simply selecting the indices to total, which will just be more complicated than the rotation algorithm would be. Also, this would only work for 2d matrices, as the 3d 90* rotation matrix is

```
[ 1 0 0 ]
[ 0 0 -1]
[ 0 1 0 ]
```
And so on. This is an ugly and brittle solution that won't support the general case of an arbitrary sized input matrix. So, we set up the rotation.

We set up vars to rotate in a familiar way:

```
left, right = 0, len(matrix) -1
```
And our loop to iterate - note we only iterate to `len[matrix] - 2` as the element at `len(matrix) - 1` would otherwise be rotated twice (once at 0, the second at len-1)
```
while left < right:
  for i in range(right - left):
    top, bot = left, right

    top_left = matrix[top][left + i]    # temp store top left

    matrix[top][left + i] = matrix[bot - i][left]      # bot left to top left
    matrix[bot - i][left] = matrix[bot][right - i]     # bot right to bot left
    matrix[bot][right - i] = matrix[top + i][right]    # top right to bot right
    matrix[top + i][right] = top_left                  # and put top left back in top right

  right -= 1
  left += 1

```

We'll step through the 3x3 example and see that this problem is really about modeling the problem in code as you would think of it intuitively.

```
1 2 3
4 5 6
7 8 9

first iter, i=0, left=top=0, right=bot=2

top_left = matrix[top][left + i]                   # 1
matrix[top][left + i] = matrix[bot - i][left]      # (7) goes to top left
matrix[bot - i][left] = matrix[bot][right - i] # (9) to bot left
matrix[bot][right - i] = matrix[top + i][right]    # (3) to bot right
matrix[top + i][right] = top_left                  # and put top left back in top right

7 2 1
4 5 6
9 8 3

second iter, i=1, left=top=0, right=bot=2 - here I will include the actual indicies to show the calculations work

top_left = matrix[top][left + i]                   # 2

matrix[top][left + i] = matrix[bot - i][left]      # (4) goes to 0,1
matrix [0]     [1]    = matrix  [1]     [0]

matrix[bot - i][left] = matrix[bot][right - i]     # (8) goes to 1,0
matrix   [1]      [0]     = matrix [2]   [1]

matrix[bot][right - i] = matrix[top + i][right]    # (6) to 2,1
matrix [2]     [1]     = matrix   [1]     [2]

matrix[top + i][right] = top_left                  # and put (2) back in 1,2

7 4 1
8 5 2
9 6 3

and since at this point, left +1 == right -1, we stop iteration and see the matrix is rotated.
```

and as an aside we can implement rotation by matrix multiplication in python anyway:

```
def rotate(matrix):
  resultant = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]

  rotate = [[0, 1], [-1, 0]]

  for i in range(len(matrix)):
      for j in range(len(rotate[0])):
          for k in range(len(rotate)):

              # resulted matrix
              resultant[i][j] += matrix[i][k] * rotate[k][j]

  return resultant


```
