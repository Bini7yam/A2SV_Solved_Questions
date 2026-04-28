#define smn(mn,n) mn = min(mn,n)
class Solution {
  public:
    int matrixMultiplication(vector<int> &arr) {
        int n = arr.size();
        const int INF = 1e9 + 19;
        vector dp(n+1,vector<int>(n+1,INF));
        for(int i=1;i<n;++i) dp[i-1][i] = 0;
        for(int i=0;i<n;++i) dp[i][i] = 0;
        for(int d=2;d<n;++d){
            for(int i=0;i+d<n;++i){
                int j = i + d;
                for(int k=i+1;k<j;++k)
                    smn(dp[i][j], dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]);
                
            }
        }
        return dp[0][n-1];
    }
};