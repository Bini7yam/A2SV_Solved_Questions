#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    int knapsack(int W, vector<int> &val, vector<int> &wt) {
        // code here
        int n = val.size();
        vector dp(n+5, vector<int>(W+3));
        for(int i=0;i<n;++i){
            for(int w=1;w<=W;++w){
                dp[i+1][w] = w >= wt[i]?dp[i][w-wt[i]]+val[i] : 0;
                smx(dp[i+1][w],dp[i][w]);
            }
        }
        return dp[n][W];
    }
};