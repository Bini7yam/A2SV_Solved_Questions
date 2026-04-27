// User function template
#define smx(mx,x) mx = max(mx,x)
#define ll long long
class Solution {
  public:
    // s : given string
    // return the expected answer
    const ll MOD = 1e9 + 7;
    int fun(string &s) {
        int n = s.length();
        ll a = 0, b = 0, c = 0;
        for(char e:s){
            if(e=='c') c = c + c + b;
            if(e=='b') b = b + b + a;
            if(e=='a') a = a + a + 1;
            c %= MOD;
            b %= MOD;
            a %= MOD;
        }
        return c;
    }
};