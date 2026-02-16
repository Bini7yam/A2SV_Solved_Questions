// User function template for C++
#define ll long long
class Solution {
  public:
    int findMaxValue(vector<int> &a) {
        // code here
        const ll INF = 1e18 + 19;
        array<ll, 4> dp = {-INF, -INF, -INF, -INF};
        int n = a.size();
        for(int i=0;i<n;++i){
            array<ll, 4> ndp;
            ndp[0] = max(-(ll)a[i], dp[0]);
            ndp[1] = max(dp[0]+a[i], dp[1]);
            ndp[2] = max(dp[1]-a[i], dp[2]);
            ndp[3] = max(dp[2]+a[i], dp[3]);
            dp = ndp;
        }
        return dp[3] < -1e13 ? -1 : dp[3];
    }
};