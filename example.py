def list_multiply(A, B):
    for i in range(len(A)):
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                ans = A[i][k]*B[k][j]
                sum += ans
            print(sum, end="\t")
        print()

list_multiply([[1,2],[3,4]], [[5, 6, 7],[7, 8, 9]])

