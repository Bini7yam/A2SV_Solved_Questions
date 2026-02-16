class Solution {
  public:
    int lcs(string &s1, string &s2) {
        // code here
        int n = s1.length(), m = s2.length();
        vector dp(n+5, vector<int>(m+5));
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j){
                if(s1[i]==s2[j])dp[i+1][j+1]=dp[i][j]+1;
                else dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1]);
            }
        }
        return dp[n][m];
    }
};
