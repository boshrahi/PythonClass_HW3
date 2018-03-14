def solution(X , A)
    for i in range(len(A))
        if A[i] == X:
        L1 = A[i:]
        for j in L1:
            count = 0
            if (j < X and j not in A[:i]):
                count += 1
                return i+count
             else:
                return i
                X = row_input()
                A = map(int, row_input().split())
                print solution(X , A)
            
        
