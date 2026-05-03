class Solution {
  public:
    int countIslands(vector<vector<char>>& g) {
        // Code here
        int n = g.size(), m = g[0].size();
        vector vs(n, vector<bool>(m));
        auto dfs = [&](auto&&self, int i, int j){
            if(i<0 || j<0 || i>=n || j>=m || vs[i][j]) return;
            if(g[i][j] == 'W') return;
            vs[i][j] = 1;
            self(self,i,j-1);
            self(self,i,j+1);
            self(self,i-1,j);
            self(self,i-1,j+1);
            self(self,i-1,j-1);
            self(self,i+1,j);
            self(self,i+1,j-1);
            self(self,i+1,j+1);
        };
        int c = 0;
        
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j){
                if(g[i][j]=='W'||vs[i][j]) continue;
                dfs(dfs,i,j);
                ++c;
            }
        }
        return c;
    }
};






