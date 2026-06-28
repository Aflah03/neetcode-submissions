class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> rank(n,1);
        vector<int> par(n);// parent of each node
        for(int i=0;i< n;i++){
            par[i] = i; // initially all components are alone , and they are parent of iteself
        }
        int count = n;
        for(int i=0;i< edges.size();i++){
            count -= Union(edges[i][0],edges[i][1],par,rank);
        }
        return count;
        
    }
    int Union(int n1,int n2, vector<int> &par,vector<int> & rank){
        int p1 = find(n1,par,rank);
        int p2  = find(n2,par,rank);
        if(p1 == p2) return 0;
        if(rank[p1] >=rank[p2]){
            par[p2] = p1;
            rank[p1]+= rank[p2];
        }else{
            par[p1] = p2;
            rank[p2] +=rank[p1];
        }
        return 1;
    }
    int find(int n1,vector<int> &par,vector<int>& rank){
        int res = n1;
        while(par[res] != res){
            par[res] = par[par[res]];
            res = par[res];
        }
        return res;
    }
};
