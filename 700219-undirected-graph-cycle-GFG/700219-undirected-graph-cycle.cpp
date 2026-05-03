#define smx(mx,x) mx = max(mx,x)
class Solution {
  public:
    bool isCycle(int V, vector<vector<int>>& edges) {
        // Code here
        int n = 0, m = edges.size();
        for(auto&v:edges) for(auto&x:v) smx(n,x+1);
        vector<int> p(n);
        for(int i=0;i<n;++i) p[i] = i;
        auto find = [&](auto&self,int x)->int{
            return x==p[x] ? x : p[x] = self(self,p[x]);
        };
        auto join = [&](int x, int y)->bool{
            int px = find(find,x);
            int py = find(find,y);
            if(py==px) return 0;
            return p[px] = py;
        };
        for(int i=0;i<m;++i){
            int u = edges[i][0], v = edges[i][1];
            if(!join(u,v)) return 1;
        }
        return 0;
    }
};