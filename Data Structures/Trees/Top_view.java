/*
   class Node 
       int data;
       Node left;
       Node right;
*/
void top_view(Node root)
{
    ArrayList<Integer> alist = new ArrayList<Integer>();
    Node head = root;
    while(head.left != null){
        head = head.left;
        alist.add(head.data); // Adding left side data to alist
    }
    final int count = alist.size(); // Calculating the size of alist
    
    for(int j=count-1;j>=0;j--){
        System.out.print(alist.get(j)+" "); // print every element  of left side 
    }
    System.out.print(root.data+" "); // print the root node
    alist.removeAll(alist); // clear alist to add right side element
    head = root; // Pointing again to the root node
    while(head.right != null){
        head = head.right;
        alist.add(head.data); // adding right side data to alist
    }
    final int count1 = alist.size(); // Again size of alist for right side
    for(int i=0;i<count1;i++){
        System.out.print(alist.get(i)+" "); // print the right elements
    }

    
}
