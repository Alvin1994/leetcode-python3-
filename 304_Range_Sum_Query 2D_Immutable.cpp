#include <vector>
class NumMatrix {
private:
    std::vector<std::vector<int>> dp;
public:
    NumMatrix(std::vector<std::vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = rows>0 ? matrix[0].size() : 0;
        dp = std::vector<std::vector<int>> (rows+1, std::vector<int>(cols+1,0));
        
        for (int r=1; r<=rows; r++) {
            for (int c=1; c<=cols; c++){
                dp[r][c] = dp[r-1][c] + dp[r][c-1] + matrix[r-1][c-1] - dp[r-1][c-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return dp[row2+1][col2+1] + dp[row1][col1] - dp[row1][col2+1] - dp[row2+1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */