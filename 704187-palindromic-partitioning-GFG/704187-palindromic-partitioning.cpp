// User function Template for C++
#define smn(mn,n) mn = min(mn,n)
class Solution {
  public:
    int palPartition(string &s) {
        // code here
        int n = s.length();
        vector pal(n, vector<bool>(n));
        for(int i=1;i<n;++i){
            pal[i][i] = 1;
            pal[i-1][i] = s[i-1]==s[i];
        }
        pal[0][0] = 1;
        for(int d=2;d<n;++d){
            for(int i=0;i+d<n;++i){
                int j = i + d;
                pal[i][j] = s[i]==s[j] && pal[i+1][j-1];
            }
        }
        const int INF = 1e9 + 19;
        vector<int> dp(n+1,INF);
        dp[0] = 0;
        for(int i=0;i<n;++i){
            for(int j=0;j<=i;++j){
                if(pal[j][i])smn(dp[i+1], dp[j]+1);
            }
        }
        return dp[n]-1;
    }
};