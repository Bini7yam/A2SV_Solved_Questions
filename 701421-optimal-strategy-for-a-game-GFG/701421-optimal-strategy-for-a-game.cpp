class Solution {
  public:
    int maximumAmount(vector<int> &arr) {
        // code here
        int n = arr.size();
        vector<int> pre(n+1);
        vector<int>&a = arr;
        for(int i=0;i<n;++i) pre[i+1]=pre[i] + arr[i];
        vector dp(n+5, vector<int>(n+5));
        for(int i=0;i<n;++i) dp[i][i]=arr[i];
        for(int ln=2;ln<=n;++ln){
            for(int j=ln-1;j<n;++j){
                int i = j - ln + 1;
                int lcs = a[i] + (pre[j+1]-pre[i+1]-dp[i+1][j]);
                int rcs = a[j] + (pre[j]-pre[i]-dp[i][j-1]);
                dp[i][j] = max(lcs,rcs);
            }
        }
        return dp[0][n-1];
    }
};