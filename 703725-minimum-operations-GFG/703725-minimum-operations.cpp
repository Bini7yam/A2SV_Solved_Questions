class Solution {
  public:
    
    int minOperation(int n) {
        int c = 0;
        while(n){
            while(n%2==0)++c,n/=2;
            ++c,--n;
        }
        return c;
    }
};