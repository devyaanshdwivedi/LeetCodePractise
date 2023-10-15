/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rob(TreeNode root) {
     int[] p=help(root);
     return Math.max(p[0],p[1]);   
    }
 int[] help(TreeNode r){
        if(r==null) return new int[2];
        int[] h=help(r.left);
        int[] d=help(r.right);
        int[] v=new int[2];
        v[0]=r.val+h[1]+d[1];
        v[1]=Math.max(h[0],h[1])+Math.max(d[0],d[1]);
        return v;
    }
}