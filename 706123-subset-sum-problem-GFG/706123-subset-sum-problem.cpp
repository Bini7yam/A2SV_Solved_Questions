class Solution {
  public:
    bool isSubsetSum(vector<int>& arr, int sum) {
        // code here
        vector<bool> dp(sum+10);
        dp[0]=1;
        for(int x:arr){
            for(int i=sum;i>=x;--i){
                if(dp[i-x]) dp[i] = 1;
            }
        }
        return dp[sum];
    }
};