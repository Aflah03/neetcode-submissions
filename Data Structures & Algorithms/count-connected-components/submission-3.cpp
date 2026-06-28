class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        unordered_map<int,vector<int>> mp;
        for(int i=0;i< edges.size();i++){
            mp[edges[i][0]].push_back(edges[i][1]);
            mp[edges[i][1]].push_back(edges[i][0]);
        }
       vector<int> visit(n,0);
       stack<int> st;
       int count = 0;
       for(int i=0;i< n;i++){
        if(visit[i] ==0){
            count++;
            st.push(i);
            visit[i] = 1;
            while(!st.empty()){
                int temp = st.top();
                st.pop();
                for(auto nei: mp[temp]){
                    if(visit[nei] ==0){
                        st.push(nei);
                        visit[nei] =1;
                    }
                }
            }
        }
        
       }

       return count;
    }
};
