'''
This program is a linear algebra calculator using NumPy. 
'''

__author__ = "Jacob Emmerson"

from email.mime import base
import numpy as np
from numpy import linalg as la
import os

def getDeterminant(matrix):
    try:
        print("\nDeterminant:")
        print(la.det(matrix).round(2))
    except:
        print("Matrix is an n x n matrix. Cannot compute determinant.")

def getInverse(matrix):
    try:
        print("\nInverse:")
        print(la.inv(matrix))
    except:
        print("Matrix is singular or determinant cannot be computed. Cannot compute inverse.")

def getTranspose(matrix):
    print("\nTranspose:")
    print(matrix.transpose())

def getEigenvalues(matrix):
    eigVal, eigVect = la.eig(matrix)
    print("\nEigen Values:")
    print(eigVal)
    print("\nEigen Vectors:")
    print(eigVect)
    print("Error Occured")

def gramSchmidt(matrix):
    Q, R = la.qr(matrix)
    print("\nOrthogonalized Matrix: ")
    print(Q)
    print("\nREF Matrix:")
    print(R)

def endProgram(matrix):
    print(os._exit(0))

calculations = {
    1 : getDeterminant,
    2 : getInverse,
    3 : getTranspose,
    4 : getEigenvalues,
    5 : gramSchmidt,
    6 : endProgram
}

def main():
    correct = 'n'
    while True: #do while loop
        try:
            preMatrix = input("Enter matrix with rows separated by ';' (e.g. 1 0; 0 1 for I of size 2): ") # very forgiving format; minimizes user error
            baseMatrix = np.matrix(preMatrix)
            print(baseMatrix)
            correct = input("Is this Correct? [Yes/No]: ")

        except: #if there is a dimension error or correct input is invalid
            print("Make sure the matrix has the correct dimensions.")
            preMatrix = None
            correct = 'n'

        if (correct[0].lower() == 'y'):
            break #breaks loop if the matrix is the correct input

    while True:
        try:
            print("1: Determinant\n2: Inverse\n3: Transpose\n4: Eignvalues and Eigenvectors\n5: Orthogonalized and REF Matrix\n6: Quit\n")
            test = int(input("What are you looking for? "))
            calculations[test](baseMatrix) #switch statement
        except:
            print("Error Occured...")



if __name__ == "__main__":
    main()