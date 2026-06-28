class Solution {
public:
    int countSubstrings(string s) {
               int res = 0;
       for(int i=0;i< s.size();i++){
            res = res+ check(s, i, i);
         
       } 
        for(int i=0;i< s.size()-1;i++){
            res  = res+check(s, i, i+1);
            
       } 
       return res;
     
    }
    int  check(string& s, int l, int r){
        int ans = 0;
        while(l >=0 && r < s.size() && s[l] == s[r]){
            l = l-1;
            r = r+1;
            ans++;
        }
        return ans;
    }
};
