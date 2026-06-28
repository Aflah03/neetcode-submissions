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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> st;
        int curr = 0;
        TreeNode* node = root;
        while(!st.empty() || node!= NULL){
            while(node!= NULL){
                st.push(node);
                node = node->left;                     
            }
            curr++;
             node = st.top();
            if(curr ==k) return node->val;
            st.pop();

            node = node->right;
        } 
        return 0;
    }
};
