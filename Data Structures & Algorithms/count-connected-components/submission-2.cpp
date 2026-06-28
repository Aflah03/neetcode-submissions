class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        unordered_map<int,vector<int>> mp;
        for(int i=0;i< edges.size();i++){
            mp[edges[i][0]].push_back(edges[i][1]);
            mp[edges[i][1]].push_back(edges[i][0]);
        }
       set<int> visit;
       stack<int> st;
       int count = 0;
       for(int i=0;i< n;i++){
        if(visit.find(i) == visit.end()){
            count++;
            st.push(i);
            visit.insert(i);
            while(!st.empty()){
                int temp = st.top();
                st.pop();
                for(auto nei: mp[temp]){
                    if(visit.find(nei) == visit.end()){
                        st.push(nei);
                        visit.insert(nei);
                    }
                }
            }
        }
        
       }

       return count;
    }
};
