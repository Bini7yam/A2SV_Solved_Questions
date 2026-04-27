
class Solution {
  public:
    int minAmount(int A[], int N) {
        if(N==1) return 0;
        if(N==2) return min(A[0],A[1]);
        vector<int> dp(N+3);
        dp[0] = 0;
        dp[1] = A[0];
        dp[2] = A[1];
        for(int i=2;i<N;++i){
            dp[i+1] = A[i] + min(dp[i], dp[i-1]);
        }
        return min(dp[N],dp[N-1]);
    }
};