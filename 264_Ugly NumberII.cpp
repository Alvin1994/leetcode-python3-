#include <vector>
class Solution {
public:
    int nthUglyNumber(int n) {
        if (n==1) { return 1; }
        std::vector<int> k(n, 1);
        int pt2=0, pt3=0, pt5=0;
        for (int i=1;i<n;i++){
            k[i] = std::min(std::min(k[pt2]*2, k[pt3]*3), k[pt5]*5);
            if (k[i]==k[pt2]*2) { pt2+=1; }
            if (k[i]==k[pt3]*3) { pt3+=1; }
            if (k[i]==k[pt5]*5) { pt5+=1; }
        }
        return k[n-1];
    }
};