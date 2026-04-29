class Solution {
public:
    bool isScramble(string s1, string s2) {
        int n = s1.length();
        bool dp[n][n][n][n];
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;++i)for(int j=0;j<n;++j)dp[i][i][j][j] = s1[i]==s2[j];
        for(int d=1;d<n;++d){
            for(int i1=0;i1+d<n;++i1){

                int j1 = i1 + d;

                for(int i2=0;i2+d<n;++i2){

                    int j2 = i2 + d;
                    bool & b = dp[i1][j1][i2][j2];
                    for(int l=0;l<d;++l){

                        int d1 = i1 + l;
                        int d2 = i2 + l;
                        b |= dp[i1][d1][i2][d2] && dp[d1+1][j1][d2+1][j2];
                        d2 = j2 - l - 1;
                        b |= dp[i1][d1][d2+1][j2] && dp[d1+1][j1][i2][d2];

                    }

                }

            }
        }
        return dp[0][n-1][0][n-1];
    }
};