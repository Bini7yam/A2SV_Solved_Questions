class Solution {
  public:
    void dfs(vector<vector<int>>&adj, vector<bool>&vs, vector<int>&lst, int x){
        if(vs[x]) return;
        vs[x] = 1;
        lst.push_back(x);
        for(int y:adj[x]) dfs(adj,vs,lst,y);
    }
    vector<int> dfs(vector<vector<int>>& adj) {
        // Code here
        int n = adj.size();
        vector<int> lst;
        vector<bool> vs(n);
        dfs(adj,vs,lst,0);
        return lst;
    }
};