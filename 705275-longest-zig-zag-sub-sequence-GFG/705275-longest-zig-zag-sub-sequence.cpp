#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    int ZigZagMaxLength(vector<int>& nums) {
        // Code here
        int n = nums.size();
        vector<int> dp0(n), dp1(n), mx, mn;
        for(int i=0;i<n;++i){
            while(!mx.empty() && nums[mx.back()] <= nums[i]) mx.pop_back();
            while(!mn.empty() && nums[mn.back()] >= nums[i]) mn.pop_back();
            dp0[i] = mn.empty() ? 1 : dp1[mn.back()] + 1;
            dp1[i] = mx.empty() ? 1 : dp0[mx.back()] + 1;
            if(mx.empty() || dp0[i] > dp0[mx.back()]) mx.push_back(i);
            if(mn.empty() || dp1[i] > dp1[mx.back()]) mn.push_back(i);
        }
        return max(dp0[n-1], dp1[n-1]);
    }
};