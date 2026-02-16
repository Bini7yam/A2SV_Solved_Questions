class Solution {
  public:
    // Function to compute the edit distance between two strings
    int editDistance(string& s1, string& s2) {
        // code here
        int n = s1.length(), m = s2.length();
        vector dp(n+5, vector<int>(m+5));
        for(int i=0;i<=n;++i) dp[i][0] = i;
        for(int i=0;i<=m;++i) dp[0][i] = i;
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j){
                if(s1[i]==s2[j])dp[i+1][j+1]=dp[i][j];
                else{
                    dp[i+1][j+1]=min({dp[i][j+1]+1,dp[i+1][j]+1,dp[i][j]+1});       
                }
            }
        }
        //cout<<dp[1][1]<<' '<<dp[0][1]<<' '<<dp[0][2]<<endl;
        return dp[n][m];
    }
};