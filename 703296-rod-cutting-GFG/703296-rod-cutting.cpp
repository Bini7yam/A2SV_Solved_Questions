// User function Template for C++

class Solution {
  public:
    int cutRod(vector<int> &price) {
        // code here
        int n = price.size();
        vector dp(n+5,vector<int>(n+5));
        //dp[i][j]=stick of length j sold using upto k
        for(int i=1;i<=n;++i){
            for(int j=1;j<=n;++j){
                if(i > j) {dp[i][j]=dp[i-1][j];continue;}
                dp[i][j] = max(dp[i-1][j], dp[i][j-i]+price[i-1]);
            }
        }
        return dp[n][n];
    }
};