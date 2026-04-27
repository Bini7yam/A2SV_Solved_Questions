class Solution {
  public:
    bool valid(char a, char b){
        if(a=='0') return 0;
        if(a > '2') return 0;
        if(a < '2') return 1;
        return b < '7';
    }
    bool valid(char a){
        return a != '0';
    }
    int countWays(string &digits) {
        // Code here
        int n = digits.length();
        vector<int> dp(n+1);
        dp[0] = 1;
        for(int i=0;i<n;++i){
            if(valid(digits[i])) dp[i+1] = dp[i]; 
            if(!i) continue;
            char a = digits[i-1], b = digits[i];
            if(valid(a,b)) dp[i+1] += dp[i-1];
        }
        return dp[n];
    }
};