#include <vector>
class Solution {
public:
    std::vector<int> countBits(int num) {
        if (num == 0) { return std::vector<int> {0}; }

        std::vector<int> dp(num+1, 0);
        int startPtr = 1;
        while (startPtr <= num){
            for (int j=startPtr;j < startPtr*2;j++){
                if (j > num) { break; }
                dp[j] = dp[j-startPtr] + 1;
            }
            startPtr *= 2;
        }
        return dp;
    }
};