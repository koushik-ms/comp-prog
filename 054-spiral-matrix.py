from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiralOrderStep(matrix, 0, 0, len(matrix), len(matrix[0]))

    def spiralOrderStep(self, matrix: List[List[int]], sr: int, sc: int, n: int, m: int) -> List[int]:
        if sr >= n or sc >= m:
            return []
        
        seq1 = matrix[sr][sc:m]
        seq2 = [row[m-1] for row in matrix[sr:n]] if m-1 >= sc else []
        seq3 = matrix[n-1][sc:m][::-1] if n-1 > sr and m-1 > sc else []
        seq4 = [row[sc] for row in matrix[sr+1:n][::-1]] if n-1 > sr  and m-1 > sc else []
        rest = self.spiralOrderStep(matrix, sr+1, sc+1, n-1, m-1)

        return seq1 + seq2[1:] + seq3[1:] + seq4[1:] + rest

if __name__ == "__main__":
    matrix = [[7],[9],[6]]
    output = [7,9,6]
    ao = Solution().spiralOrder(matrix)
    print(f"Matrix:    {matrix}")
    print(f"Expected:  {output}")
    print(f"Actual:    {ao}")
