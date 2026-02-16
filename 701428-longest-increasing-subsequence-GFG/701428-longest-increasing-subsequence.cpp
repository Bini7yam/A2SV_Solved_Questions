class Solution {
  public:
    int lis(vector<int>& arr) {
        // code here
        set<int> dp;
        for(int x:arr){
            auto it = lower_bound(dp.begin(),dp.end(),x);
            if(it==dp.end()) dp.insert(x);
            else dp.erase(it),dp.insert(x);
        }
        return dp.size();
    }
};