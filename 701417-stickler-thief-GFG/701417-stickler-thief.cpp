class Solution {
  public:
    int findMaxSum(vector<int>& a) {
        // code here
        int n = a.size();
        vector<int> dp(n+5);
        if(n==1) return a[0];
        if(n==2) return max(a[0],a[1]);
        if(n==3) return max(a[0]+a[2],a[1]);
        dp[0] = a[0];
        dp[1] = a[1];
        dp[2] = a[0] + a[2];
        for(int i=3;i<n;++i){
            dp[i] = a[i] + max(dp[i-2],dp[i-3]);
        }
        return max(dp[n-1],dp[n-2]);
    }
};