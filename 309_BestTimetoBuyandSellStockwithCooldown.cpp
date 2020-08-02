#include <vector>
class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int hold = INT_MIN, rest=0, sold=0;

        for (int price: prices){
            hold = std::max(rest-price, hold);
            rest = std::max(rest, sold);
            sold = hold + price;
        }
        return std::max(sold,rest);
    }
};