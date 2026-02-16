
class Solution {
    
    #define ll long long
  public:
    // Function to find the nth catalan number.
    int findCatalan(int n) {
        // code here
        ll res = 1;
        for(int i=1;i<=n;++i){
            ll pro = n+i, dv = i;
            ll g=__gcd(pro,dv);
            pro/=g,dv/=g;
            g = __gcd(res,dv);
            res/=g,dv/=g;
            res *= pro;
            res /= dv;
        }
        return (int)(res/(n+1));
    }
};
