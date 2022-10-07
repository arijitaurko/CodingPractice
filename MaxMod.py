class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        modValue = []
        for i in range(len(A)):
            for j in range(i):
                if(A[i] != 0 and A[j] !=0):
                    modValue.append(A[i] % A[j])
                else:
                    continue
            for j in range(i+1, len(A)):
                if(A[i] != 0 and A[j] !=0):
                    modValue.append(A[i] % A[j])
                else:
                    continue

        return max(modValue)

    