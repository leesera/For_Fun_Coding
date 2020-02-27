matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
"""
first
1...2 --> 4...1
.....     .....
4...3     3...2
dep = 0
snd
.... ---> ....
.12.      .41.
.43.      .32.
....      ....
dep=1
"""

def lotateMatrix(matrix):
  for dep in range(int(len(matrix[0])/2)):
    lotateMatrixWithDepth(matrix,dep)
  return matrix

def lotateMatrixWithDepth(matrix,dep):
  N = len(matrix)
  for idx in range(N-2*dep):
    fst = matrix[dep][idx+dep]
    print(idx)
    print(fst)
    snd = matrix[dep+idx][N-dep-1]
    print(snd)
    trd = matrix[N-1-dep][N-dep-1-idx]
    fourth = matrix[N-1-dep-idx][dep]
    matrix[dep][dep+idx] = fourth
    matrix[dep+idx][N-dep-1] = fst
    matrix[N-1-dep][N-dep-1-idx] = snd
    matrix[N-1-dep-idx][dep] = trd

def print_matrix(matrix):
  for m in matrix:
    for e in m:
      print(e, end=" ")
    print()
print_matrix(matrix) 
print()
print_matrix(lotateMatrix(matrix))

