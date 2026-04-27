class Solution {
  public:
    string getLongestPal(string &s) {
        int n = s.length();
        int mx = 1;
        int st = 0;
        for(int i=0;i<n;++i){
            int l = i, r = i;
            while(l > 0 && r<n-1){
                if(s[l-1] == s[r+1]) --l,++r;
                else break;
            }
            int rng = r - l + 1;
            if(rng > mx){
                mx = rng;
                st = l;
            }
        }
        for(int i=1;i<n;++i){
            int l = i-1, r = i;
            if(s[i]-s[i-1]) continue;
            while(l > 0 && r<n-1){
                if(s[l-1] == s[r+1]) --l,++r;
                else break;
            }
            int rng = r - l + 1;
            if(rng > mx){
                mx = rng;
                st = l;
            }
        }
        return s.substr(st,mx);
    }
};