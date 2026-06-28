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
       for(auto item:  mp){
        if(visit.find(item.first) == visit.end()){
            count++;
            st.push(item.first);
            visit.insert(item.first);
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
       if(mp.size() != n){
        return count+ n-mp.size();
       }
       return count;
    }
};
