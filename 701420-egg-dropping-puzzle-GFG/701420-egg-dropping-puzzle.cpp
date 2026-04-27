#define smn(mn,n) mn = min(mn,n)
class Solution {
  public:

    // Function to find minimum number of attempts needed in
    // order to find the critical floor.
    int eggDrop(int n, int k) {
        const int INF = 1e5 + 15;
        //dp[egg][step]
        //
        vector dp(n+1,vector<int>(k+1,INF));
        for(int j=0;j<=k;++j) dp[1][j] = j;
        for(int i=0;i<=n;++i) dp[i][0] = 0;
        
        for(int i=2;i<=n;++i){
            int d = 1;
            for(int j=1;j<=k;++j){
                
                while(d<k&&dp[i-1][d-1]<dp[i][j-d])++d;
                
                int v=1+max(dp[i-1][d-1],dp[i][j-d]);
                
                smn(dp[i][j],v);
                
            }
        }
        return dp[n][k];
    }
};