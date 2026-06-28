class Solution {
public:
    vector<int> countBits(int n) {
        int k = 1;
        vector<int> ans(n+1,0);
        for(int i=1;i<=n;i++){
            if(k*2 == i) k*=2;
            ans[i] = 1 + ans[i-k];
        }
        return ans;
    }
};
