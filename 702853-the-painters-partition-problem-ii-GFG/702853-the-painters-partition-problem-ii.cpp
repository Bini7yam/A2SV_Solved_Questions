#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    int minTime(vector<int>& arr, int k) {
        // code here
        int n = arr.size();
        int mx = 0, ttl = 0;
        for(int x:arr)smx(mx,x), ttl += x;
        int l = mx, r = ttl, d;
        while(l <= r){
            int m = (l+r)/2;
            int c = 1, rn = 0;
            for(int x:arr){
                if(x + rn > m){
                    ++c;
                    rn = x;
                }else rn += x;
            }
            if(c > k) l = m + 1;
            else r = m - 1, d = m;
            
        }
        return d;
    }
};