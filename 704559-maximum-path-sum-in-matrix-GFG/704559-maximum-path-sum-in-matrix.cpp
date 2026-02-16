// User function Template for C++
#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    int maximumPath(vector<vector<int>>& mat) {
        // code here
        int n = mat.size(),m = mat[0].size();
        vector dp(n+5, vector<int>(m+5));
        int mx = 0;
        for(int i=0;i<m;++i) dp[0][i] = mat[0][i],smx(mx,mat[0][i]);              
        
        for(int i=1;i<n;++i){
            for(int j=0;j<m;++j){
                smx(dp[i][j], dp[i-1][j]);
                if(j) smx(dp[i][j], dp[i-1][j-1]);
                if(j!=m-1)smx(dp[i][j],dp[i-1][j+1]);
                dp[i][j] += mat[i][j];
                smx(mx, dp[i][j]);
            }
        }
        return mx;
    }
};