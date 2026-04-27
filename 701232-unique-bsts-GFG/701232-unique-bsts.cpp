class Solution {
  public:
    // Function to return the total number of possible unique BST.
    int numTrees(int n) {
        // Your code here
        vector<int> dp(n+1);
        dp[0] = 1;
        for(int i=1;i<=n;++i){
            for(int l = 0; l < i; ++l){
                int r = i - l - 1;
                dp[i] += dp[l] * dp[r];
            }
        }
        return dp[n];
    }
};