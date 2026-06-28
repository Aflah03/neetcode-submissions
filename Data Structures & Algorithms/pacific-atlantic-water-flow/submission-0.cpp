class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        set<pair<int,int>> P;
        set<pair<int,int>> A;
        int rows = heights.size();
        int cols = heights[0].size();
        for(int r=0;r<rows;r++){
            for(int c =0;c< cols;c++){
                if(r==0 || c==0) P.insert({r,c});
                if(r==rows-1 || c == cols-1) A.insert({r,c});
            }
        } 
        vector<pair<int,int>> neighbors = {{0,1},{0,-1},{1,0},{-1,0}};
        queue<pair<int,int>> q;
        set<pair<int,int>> visit;
        for(auto item: P){
            q.push(item);
            visit.insert(item);
        }
        while(!q.empty()){
            auto temp = q.front();
            q.pop();
            for(auto nei: neighbors){
                int rr = temp.first+ nei.first;
                int cc = temp.second+ nei.second;
                if(visit.find({rr,cc}) == visit.end() 
                && rr < rows && cc < cols && cc>=0 && rr >=0){
                    if(heights[rr][cc] >= heights[temp.first][temp.second]){
                        q.push({rr,cc});
                        P.insert({rr,cc});
                        visit.insert({rr,cc});
                    }
                }
            }
        }
        for(auto item: P){
            cout << "[" << item.first << ", " << item.second << " ]";
            cout << " ,";
        }
        q = queue<pair<int,int>>();
        visit.clear();
        for(auto item: A){
            q.push(item);
            visit.insert(item);
        }
        while(!q.empty()){
            auto temp = q.front();
            q.pop();
            for(auto nei: neighbors){
                int rr = temp.first+ nei.first;
                int cc = temp.second+ nei.second;
                if(visit.find({rr,cc}) == visit.end() 
                && rr < rows && cc < cols && cc>=0 && rr >=0){
                    if(heights[rr][cc] >= heights[temp.first][temp.second]){
                        q.push({rr,cc});
                        A.insert({rr,cc});
                        visit.insert({rr,cc});
                    }
                }
            }
        }
        cout << endl << "A: " << endl; 
        for(auto item: A){
            cout << "[" << item.first << ", " << item.second << " ]";
            cout << " ,";
        }
        vector<vector<int>> ans;
        for(auto item: P){
            if(A.find(item) != A.end()){
                ans.push_back({item.first,item.second});
            }
        }
        return ans;
    }
};
