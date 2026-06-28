    class Solution {
    public:
        bool validTree(int n, vector<vector<int>>& edges) {
            vector<vector<int>> g(n);
            for(int i=0;i< edges.size();i++){
                g[edges[i][0]].push_back(edges[i][1]);
                g[edges[i][1]].push_back(edges[i][0]); 
            }
            vector<int> visited(n,0);
            visited[0]  = 1;
            bool ans = dfs(0,-1,visited,edges,g);
            if(ans == false) return false;
            cout << "visited: ";
            for(int i=0;i< n;i++){
                cout << visited[i] << " ";
            }
            for(int i=0;i< n;i++){
                if(visited[i] ==0) return false;
            }
            return true;
        }
        bool dfs(int node,int prev, vector<int> &visited,vector<vector<int>>& edges,vector<vector<int>> &g ){
            for(int i=0;i< g[node].size();i++){
                if(visited[g[node][i]] ==1 && g[node][i] != prev) return false;
                if(g[node][i] == prev) continue;
                visited[g[node][i]] = 1;
                dfs(g[node][i],node,visited,edges,g);
            }
            return true;


        }
    };
