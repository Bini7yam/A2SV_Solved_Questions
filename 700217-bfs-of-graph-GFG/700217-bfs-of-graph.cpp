class Solution {
  public:
    vector<int> bfs(vector<vector<int>> &adj) {
        // code here
        int n = adj.size();
        vector<int> lst;
        vector<bool> vs(n);
        vs[0] = 1;
        queue<int> q;
        q.push(0);
        while(!q.empty()){
            int x = q.front();
            lst.push_back(x);
            q.pop();
            for(int y:adj[x]){
                if(vs[y]) continue;
                vs[y] = 1;
                q.push(y);
            }
        }
        return lst;
    }
};