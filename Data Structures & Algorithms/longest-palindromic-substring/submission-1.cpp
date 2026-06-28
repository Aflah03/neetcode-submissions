class Solution {
public:
    string longestPalindrome(string s) {
               int maxLen = 1;
               string res = "";
       for(int i=0;i< s.size();i++){
            string odd =  check(s, i, i);
            if(odd.size() > res.size()) res = odd;
       } 
        for(int i=0;i< s.size()-1;i++){
            string even =  check(s, i, i+1);
            if(even.size() > res.size()) res = even;
       } 
       return res;
     
    }
    string check(string& s, int l, int r){
        while(l >=0 && r < s.size() && s[l] == s[r]){
            l = l-1;
            r = r+1;
        }
        r = r-1;
        l = l+1;
        return s.substr(l,r-l+1);
    }
    
};
