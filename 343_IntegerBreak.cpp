#include <vector>
class Solution {
public:
    int integerBreak(int n) {
        return integerBreak_while(n);
    }
    // while solution, val = 3*k + c. time o(k + 1), space(o(1))
    int integerBreak_while(int n) {
        if ( n==2 || n == 3) { return n-1; }
        int res = 1;
        while (n > 4){
            n -= 3;
            res *= 3;
        }
        return res * n;
    }
    // dp solution, time o(n), space(n+1)
    int integerBreak_dp(int n) {
        if ( n==2 || n == 3) { return n-1; }
        if ( n==4 ) {return 4;}
        std::vector<int> dp{0,0,1,2,4,6,9};
        for (int i = 7; i <= n; i++){
            dp.push_back(dp[i-3]*3);
        }
        return dp[n];
    }
    // dp optimization, time o(n), space o(3)
    int integerBreak_optimization(int n) {
        if ( n==2 || n == 3) { return n-1; }
        std::vector<int> dp{4,6,9}; // 4 , 5 , 6
        // mapping from 7,8,9,10,11,12 to 0,1,2,0,1,2
        for (int i = 7; i <= n; i++){
            dp[(i-1)%3] = dp[(i-1)%3] * 3;
        }
        return dp[(n-1)%3];
    }
};