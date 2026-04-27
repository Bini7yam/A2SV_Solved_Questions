#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    int maxSumIS(vector<int>& arr) {
        // code here
        int n = arr.size(), res = 0;
        vector<int> dp(n);
        for(int i=0;i<n;++i){
            dp[i] = arr[i];
            for(int j=0;j<i;++j){
                if(arr[j] < arr[i]) smx(dp[i], dp[j] + arr[i]);
            }
            smx(res, dp[i]);
        }
        return res;
    }
};