/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node == NULL) return NULL;
       unordered_map<Node*,Node*> mp;
       return dfs(node,mp);
 
    }
    Node* dfs(Node* node,unordered_map<Node*,Node*>& mp ){
        if(mp.count(node) !=0){
            return mp[node];
        }    
        Node* temp = new Node(node->val);
        mp[node] = temp;
        for(auto nei: node->neighbors){
            temp->neighbors.push_back(dfs(nei,mp));
        }
        return temp;
    }
};
