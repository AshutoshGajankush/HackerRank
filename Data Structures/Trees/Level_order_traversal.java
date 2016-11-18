   /* 
    
    class Node 
       int data;
       Node left;
       Node right;
   */
//import java.util.*;
   void LevelOrder(Node root)
    {
      java.util.LinkedList<Node> que = new java.util.LinkedList<Node>();
       que.add(root);
       while(que.peekFirst() != null){
           Node current = que.poll();
           System.out.print(current.data+" ");
            if(current.left != null){
                que.add(current.left);
            }
            if (current.right != null){
                que.add(current.right);
            }
    }
   }