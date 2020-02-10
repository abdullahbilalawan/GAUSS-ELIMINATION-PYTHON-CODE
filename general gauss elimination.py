import numpy
import math


# defining a matrix
# steps of gauss elimination'
# 1 make 1st element of row equal to 1
# make elements under it to 0
# make second row pivot be 1
# make zero under it

# heading

print("============================================GAUSS ELIMINATION FOR 3 VARIABLES ========================================================")


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$  ENTER THE ELEMENTS OF THE AUGMENTED MATRIX A VERY CAREFULY $$$$$$$$$$$$$$$$$$$$$$$$$$$")

variable = int(input("Enter no of distinct variables: "))
A = []
for m in range(1,variable+1):
    print("Enter values of {} equation using , as seperator".format(m))
    row = input("Eqa{}: \t".format(m)).split(',')
    for element in row: element = int(element)
    A.append(row)
# taking inputs
# creating the matrix

A = numpy.array(A, dtype='f')
pivot = 0
print("The Initial Array is: \n",A,"\n")
#making the first element 1 and 0,s under it

for j in range(0,variable):
    if A[j][j] != 0:
        A[j] = numpy.true_divide(A[j],A[j][j])
    for i in range(j+1,variable):
        if A[i][j] != 0:
            A[i] = A[i] - A[i][j]*A[j]


        else:
            A[i] = A[i][j] * A[j] + A[i]
    print('~\n',A,'\n')
# solving the equations
print('~\n',A,'\n')
coeffecient_matrix = A[0:variable,:variable]
print('coeffecient matrix is:\n',coeffecient_matrix)
B_matrix = A[:variable,variable:variable+1]
print('b matrix is:\n',B_matrix)

try:
    Answer = numpy.linalg.solve(coeffecient_matrix,B_matrix)

    print("the answer of variables in order are")
    #print("x=",Answer[0],"y=",Answer[1],"z=",Answer[2])
    print(Answer)

    #print("if answer is nan , it shows that the linear system has infinite or no solution")
except numpy.linalg.LinAlgError:
    print("No Solution Exits.")














