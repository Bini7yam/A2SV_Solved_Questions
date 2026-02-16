class Solution {
  public:
    int countWays(int n) {
        // your code here
        vector<int> dp(n+5);
        dp[0] = 1;
        for(int i=0;i<n;++i){
            dp[i+1] += dp[i];
            dp[i+2] += dp[i];
        }
        return dp[n];
    }
};
