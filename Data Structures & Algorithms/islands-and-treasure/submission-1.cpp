class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<int>> visit(rows, vector<int>(cols,0));
        queue<pair<int,int>> q;
        for(int r=0;r<rows;r++){
            for(int c=0;c< cols;c++){
                if(grid[r][c] ==0){
                    q.push({r,c});
                    visit[r][c] =1;
                }
            }
        }
        int level =0;
        while(!q.empty()){
            int n = q.size();
            level++;
            for(int i=0;i< n;i++){
                auto temp = q.front();
                q.pop();
                vector<pair<int,int>> directions = {{0,1},{0,-1},{-1,0},{1,0}};
                for(auto x : directions){
                    int rr = temp.first+ x.first;
                    int cc = temp.second+ x.second;
                    if( rr < rows && cc < cols && rr >=0 && cc >=0 && visit[rr][cc]==0
                    && grid[rr][cc] ==2147483647){
                        grid[rr][cc] = level;
                        visit[rr][cc]=1;
                        q.push({rr,cc});
                    }
                }
            }
        }



    }
};
