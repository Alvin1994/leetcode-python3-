#include <vector>
#include <limits>

class Solution {
public:
    /** state machine*/
    /**
     * |     H1     |     H2     |
     * | buy | sell | buy | sell |
     */ 
    int maxProfit(std::vector<int>& prices){
        if (prices.size()==0 || prices.size()==1) { return 0; }
        int K=2;
        std::vector<int> dp(2*K+1, std::numeric_limits<int>::min());
        dp[0]= 0; /** avoid overflow */
        dp[1] = -prices[0];
        for (auto &p:prices){
            for (int k=0;k<K;k++){
                /** find max profit on buy operation */
                dp[2*k+1] = std::fmax(dp[2*k+1], dp[2*k]-p);
                /** find max profit on sell operation */
                dp[2*k+2] = std::fmax(dp[2*k+2], dp[2*k+1]+p);
            }
        }
        return dp[2*K];
    }
    /** dp o(n^2)*/
    int maxProfit2(std::vector<int>& prices) {
        if (prices.size()==0 || prices.size()==1) { return 0; }
        int K=2;
        /** i x k+1 */
        std::vector<std::vector<int>> dp(prices.size(), std::vector<int> (K+1, 0));
        
        for (int k=1;k<=K; k++){
            for (int i=1; i<prices.size(); i++){
                /** dp[i][k] = (prices[i] - prices[j]) + dp[j-1][k-1], i > j */
                int min = std::numeric_limits<int>::max();
                for(int j=0; j < i; j++){
                    min = std::fmin(min, prices[j]-dp[j][k-1]);
                }
                dp[i][k] = std::fmax(dp[i-1][k], prices[i]-min);
            }
        }
        return dp[prices.size()-1][K];
    }
};
