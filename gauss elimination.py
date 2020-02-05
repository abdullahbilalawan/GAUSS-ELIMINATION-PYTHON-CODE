import numpy
import math


# defining a matrix
#steps of gauss elimination'
# 1 make 1st element of row equal to 1
# make elements under it to 0
# make second row pivot be 0
# make zero under it

# heading

print("============================================GAUSS ELIMINATION FOR 3 VARIABLES ========================================================")


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$  ENTER THE ELEMENTS OF THE AUGMENTED MATRIX A VERY CAREFULY $$$$$$$$$$$$$$$$$$$$$$$$$$$")


# taking inputs
row_1 = [int(input("x1= ")),int(input("y1=")),int(input("z1=")),int(input("b1=")), ]
row_2 = [int(input("x2=")),int(input("y2=")),int(input("z2=")),int(input("b2=")), ]
row_3 = [int(input("x3=")),int(input("y3=")),int(input("z3=")),int(input("A34=")), ]






# creating the matrix

A = numpy.array([row_1,row_2,row_3], dtype='f')
pivot = 0


#making the first element 1 and 0,s under it


if A[0][0] !=1:

    A[0] = numpy.true_divide(A[0],A[0][0])

    for i in range(1,3):
        if A[:,0][i] != 0 and A[:,0][i]>0:
            A[i] = A[:,0][i]*A[0] - A[i]


        else:
            A[i] = A[:, 0][i] * A[0] + A[i]
else:
    for i in range(1,3):
        if A[:,0][i] != 0 and A[:,0][i]>0:
            A[i] = A[:,0][i]*A[0] - A[i]


        else:
            A[i] = A[:, 0][i] * A[0] + A[i]






# making the pivot in second row and 0,s under it

if A[1][1] !=1:

    A[1] = numpy.true_divide(A[1],A[1][1])

    for i in range(2,3):
        if A[:,1][i] != 0 and A[:,1][i]>0:
            A[i] = A[:,1][i]*A[1] - A[i]

        else:
            A[i] = A[:, 1][i] * A[1] + A[i]




# making the last pivot

if A[2][2]!=1:
    A[2] = A[2] / A[2][2]





# solving the equations

coeffecient_matrix = A[0:3,:3]
B_matrix = A[:3,3:4]


Answer = numpy.linalg.solve(coeffecient_matrix,B_matrix)



print("the answer of three variables are")
print("x=",Answer[0],"y=",Answer[1],"z=",Answer[2])

print("if answer is nan , it shows that the linear system has infinite or no solution")















