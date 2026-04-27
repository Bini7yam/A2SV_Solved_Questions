#define smn(mn,n) mn = min(mn,n)
class Solution {
  public:
    int minJumps(vector<int>& arr) {
        // code here
        const int INF = 1e7 + 18;
        multiset<int> mn;
        int n = arr.size();
        vector<int> dp(n,INF), t(n,INF);
        dp[0] = t[0] = 0;
        mn.insert(0);
        for(int i=0;i<n;++i){
            if(mn.empty()) return -1;
            smn(dp[i], *mn.begin());
            if(t[i] != INF) mn.erase(mn.find(t[i]));
            if(!arr[i]) continue;
            int j = min(n-1, i+arr[i]);
            if(dp[i]+1 < t[j]){
                if(t[j]-INF) mn.erase(mn.find(t[j]));
                t[j] = dp[i]+1;
                mn.insert(t[j]);
            }
        }
        return dp[n-1];
    }
};
