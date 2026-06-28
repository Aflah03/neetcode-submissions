class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int cols = grid[0].size();
        int rows = grid.size();
        vector<vector<int>> visited(rows,vector<int>(cols,0));
        queue<pair<int,int>> q;
        for(int r = 0;r< rows;r++){
            for(int c =0; c< cols;c++){
                if(grid[r][c] ==0){
                    q.push({r,c});
                }
            }
        }
        int dist = 0;
        while(!q.empty()){
            int n = q.size();
             dist+=1;
            for(int i=0;i< n;i++){
                    auto x = q.front();
                    q.pop();
                    int  r = x.first;
                    int c = x.second;
                    visited[r][c] = 1;
                    vector<pair<int,int>> directions = {{0,1},{0,-1},{1,0},{-1,0}};
                    for(auto dir : directions){
                        int rr = dir.first+ r;
                        int cc = dir.second+ c;
                        if(rr < rows && cc < cols && rr >=0 && cc >=0 
                        && visited[rr][cc]==0 && grid[rr][cc]!=-1){
                            visited[rr][cc]=1;
                            grid[rr][cc]= dist;
                            q.push({rr,cc});
                        }
                    }
            }
           
        }
    }
    
};
