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
        queue<pair<TreeNode*, int>> q;
        if(!root) return 0;
        q.push({root, 1});
        int ans = 1;
        int depth  =0;
        while(!q.empty()){
            for(int i=0;i< q.size();i++){
                pair<TreeNode*, int> item = q.front();

            q.pop();
            depth = item.second;
            ans = max(ans, depth);
            if(item.first->left) q.push({item.first->left, depth+1});
            if(item.first->right) q.push({item.first->right, depth+1});
            }
            
        } 
        return ans;
    }
};
