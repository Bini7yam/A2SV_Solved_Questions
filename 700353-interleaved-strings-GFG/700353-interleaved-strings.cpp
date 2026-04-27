class Solution {
  public:
    bool isInterleave(string &s1, string &s2, string &s3) {
        // code here
        int n1=s1.length(),n2=s2.length(),n3=s3.length();
        if(n1+n2!=n3)return 0;
        vector dp(n1+1,vector<bool>(n2+1));
        dp[0][0] = 1;
        for(int i1=0;i1<=n1;++i1){
            for(int i2=0;i2<=n2;++i2){
                if(!dp[i1][i2]) continue;
                if(i1<n1 && s1[i1] == s3[i1+i2])dp[i1+1][i2]=1;
                if(i2<n2 && s2[i2] == s3[i1+i2])dp[i1][i2+1]=1;
            }
        }
        return dp[n1][n2];
    }
};