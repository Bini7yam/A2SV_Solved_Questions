/*You are required to complete below method */
#define ll long long
class Solution {
  public:
    int minSum(vector<int>& arr) {
        // Write your code here
        int n = arr.size();
        vector<int>&a = arr;
        if(n < 4) return *min_element(arr.begin(), arr.end());
        vector<ll> dp(n+5);
        for(int i=0;i<4;++i) dp[i] = a[i];
        for(int i=4;i<n;++i){
            dp[i] = a[i] + min({dp[i-1], dp[i-2], dp[i-3], dp[i-4]});      
        }
        return min({dp[n-1], dp[n-2], dp[n-3], dp[n-4]});
    }
};