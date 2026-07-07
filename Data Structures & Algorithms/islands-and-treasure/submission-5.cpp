class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        queue<pair<int,int>> q;
        vector<vector<int>> visited(r, vector<int> (c, 0));
        for(int i=0;i< r;i++){
            for(int j = 0;j < c; j++){
                if(grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }
        vector<pair<int,int>> directions = {{0,1}, {0, -1}, {1, 0}, {-1, 0}};
        int level = 1;
        while(!q.empty()){
            int s = q.size();
            for(int k = 0;k < s;k++){
                auto [rr, cc] = q.front();
                q.pop();
                for(auto [first, second]: directions){
                    int rval = rr+ first;
                    int cval = cc + second;
                    if(rval >=0 && cval>=0 && rval< r && cval< c && grid[rval][cval] ==INT_MAX &&
                     visited[rval][cval] == 0){
                        cout << "We are entering this block " << endl;
                        grid[rval][cval] = level;
                        visited[rval][cval]=1;
                        q.push({rval,cval});
                    }
                }
            }
            level++;
            
        }
    }
};
