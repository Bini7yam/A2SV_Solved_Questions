
class Solution {
  public:
    // Function to count the number of ways in which frog can reach the top.
    int countWays(int n) {
        vector<int> dp(n+5);
        dp[0] = 1;
        for(int i=0;i<n;++i){
            dp[i+1]+=dp[i];
            dp[i+2]+=dp[i];
            dp[i+3]+=dp[i];
        }
        return dp[n];
    }
};
