    class Solution {
    public:
        bool validTree(int n, vector<vector<int>>& edges) {
            vector<vector<int>> g(n);
            if(edges.size() != n- 1 ) return false;
            for(int i=0;i< edges.size();i++){
                g[edges[i][0]].push_back(edges[i][1]);
                g[edges[i][1]].push_back(edges[i][0]); 
            }
            vector<int> visited(n,0);
            bool ans = dfs(0,-1,visited,g);
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
        bool dfs(int node,int prev, vector<int> &visited,vector<vector<int>> &g ){
            visited[node] = 1;
            for(auto nbr: g[node]){
                if(nbr == prev) continue;
                if(visited[nbr] ==1 )return false;
               if(!dfs(nbr,node,visited,g)) return false;
            }
            return true;


        }
    };
