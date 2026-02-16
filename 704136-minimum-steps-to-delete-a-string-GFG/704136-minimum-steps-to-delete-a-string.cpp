#define smn(mn,n) mn = min(mn,n)
#define smx(mx,x) mx = max(mx,x)
class Solution {

  public:
    const int INF = 1e9 + 19;
    int solve(string s){
        int n = s.length();
        vector dp(n+3, vector<int>(n+3,INF));
        if(n==1) return 1;
        if(n==2) return 2 - (s[0]==s[1]);
        for(int i=0;i<n;++i) dp[i][i] = 1;
        for(int i=1;i<n;++i) dp[i-1][i] = 2 - (s[i]==s[i-1]);
        for(int ln = 3;ln<=n;++ln){
            for(int j=ln-1;j<n;++j){
                int i = j - ln + 1;
                dp[i][j] = s[i]==s[j]?dp[i+1][j-1]:INF;
                for(int k=i;k<j;++k) smn(dp[i][j], dp[i][k]+dp[k+1][j]);
            }
        }
        return dp[0][n-1];
    }
    int minStepToDeleteString(string s) {
        return solve(s);
    }
};