class Solution {
  public:
    bool equalPartition(vector<int>& arr) {
        // code here
        int sm = 0,n = arr.size();
        for(int x:arr) sm+=x;
        vector<bool> dp(sm/2+5);
        dp[0] = 1;
        for(int x:arr){
            for(int j=sm/2;j>=x;--j) dp[j] = dp[j] | dp[j-x];
        }
        if(sm&1) return false;
        return dp[sm/2];
    }
};