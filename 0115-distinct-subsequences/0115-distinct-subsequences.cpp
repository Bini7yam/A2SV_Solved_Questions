class Solution {
public:
    int numDistinct(string s, string t) {
        int ns = s.length(), nt = t.length();
        vector<int> ind[256];
        vector<unsigned int> dp(nt+1);
        for(int i=nt-1;i+1;--i) ind[t[i]].push_back(i+1);
        dp[0] = 1;
        for(char c:s) for(int i: ind[c]) dp[i] += dp[i-1];
        return dp[nt];
    }
};