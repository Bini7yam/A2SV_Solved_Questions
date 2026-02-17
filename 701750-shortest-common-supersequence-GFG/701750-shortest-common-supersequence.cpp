class Solution {
  public:
    int minSuperSeq(string &s1, string &s2) {
        // code here
        int n1 = s1.length(), n2 = s2.length();
        vector dp(n1+5,vector<int>(n2+5));
        for(int i=0;i<=n1;++i) dp[i][0] = i;
        for(int i=0;i<=n2;++i) dp[0][i] = i;
        for(int i=0;i<n1;++i){
            for(int j=0;j<n2;++j){
                if(s1[i]==s2[j])dp[i+1][j+1]=1+dp[i][j];
                else{
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j])+1;
                }
            }
        }
        return dp[n1][n2];
    }
};