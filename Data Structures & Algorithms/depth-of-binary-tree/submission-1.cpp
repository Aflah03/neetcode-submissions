/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
       if(!root) return 0;
        stack<pair<TreeNode*,int>> st;
        int height = 0;
        int ans = 0;
        
        st.push({root,1});
        while(!st.empty()){
            pair<TreeNode*,int> item = st.top();
            st.pop();
            height = item.second;
            ans = max(ans, height);
            if(item.first->left) st.push({item.first->left, height+1});
            if(item.first->right) st.push({item.first->right, height+1});
        }
        return ans;

    }
};
