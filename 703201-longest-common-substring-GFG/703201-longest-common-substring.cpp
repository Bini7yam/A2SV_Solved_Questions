#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    int longCommSubstr(string& s1, string& s2) {
        // code here
        int n1 = s1.length(), n2 = s2.length();
        int res = 0;
        vector dp(n1+1,vector<int>(n2+1));
        for(int i1=0;i1<n1;++i1){
            for(int i2=0;i2<n2;++i2){
                if(s1[i1]!=s2[i2])continue;
                dp[i1+1][i2+1] = 1 + dp[i1][i2];
                smx(res, dp[i1+1][i2+1]);
            }
        }
        return res;
    }
};