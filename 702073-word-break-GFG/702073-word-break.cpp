class Solution {
  public:
    bool wordBreak(string &s, vector<string> &dictionary) {
        // code here
        int n = s.length();
        unordered_set<string> st;
        for(auto x:dictionary)st.insert(x);
        vector<bool> dp(n+1);
        dp[0] = 1;
        for(int i=0;i<n;++i){
            if(!dp[i])continue;
            string t;
            for(int j=i;j<n;++j){
                t += s[j];
                if(st.count(t))dp[j+1]=1;
            }
            if(dp[n]) return 1;
        }
        return 0;
        
    }
};