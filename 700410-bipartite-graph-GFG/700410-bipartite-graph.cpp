class Solution {
  public:
    bool isBipartite(int V, vector<vector<int>> &edges) {
        // Code here
        int n = V;
        vector<bool> clr(n),vs(n);
        vector adj(n, vector<int>());
        for(auto&e:edges){
            int u = e[0],v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        auto dfs =[&](auto&self,int x, bool c)->bool{
            if(vs[x]) return clr[x] ^ c;
            vs[x] = 1;
            clr[x] = c;
            for(int y:adj[x]) if(self(self,y,c^1)) return 1;
            return 0;
        };
        for(int i=0;i<n;++i){
            if(vs[i]) continue;
            if(dfs(dfs,i,0)) return 0;
        }
        return 1;
    }
};