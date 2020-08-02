#include <vector>
class Solution {
public:
    int numSquares(int n) {
        std::vector<int> k(n+1, INT_MAX);
        k[0] = 0;
        for (int num=1;num<n+1;num++){
            for (int j=1;j*j<=num;j++){
                k[num] = std::min(k[num], k[num-j*j]+1);
            }
        }
        return k[n];
    }
};