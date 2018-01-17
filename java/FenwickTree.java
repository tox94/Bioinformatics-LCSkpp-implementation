/** @author Toni Bakarcic */
/** class for creating a FenwickTree - a type of a Binary Index Tree (BIT) structure*/

public class FenwickTree {
	//private variables for storing nodes and the length of each string
	private Node[] nodes;
	private int size;

	// simple contructor
	public FenwickTree(int k) {
		this.nodes = StartArray(k + 1);
		this.size = k + 1;
	}
	
	// Procedure that returns the node with the maximum size in the range [0,i]
	// The complexity is O(log n)
	public Node get(int i) {
		Node n = new Node();
		int res = 0;
		i += 1 ;
		while(i > 0) {
			Node temp = this.nodes[i];
			if (temp.getLen() > res) {
				res = temp.getLen();
				n = temp;
			}
			// next index is calculated by removing the most significant bit
			i -= (i&-i);
		}
		return n;
	}
	
	// Procedure that updates the BIT
	// The complexity is O(log n)
	public void update(int i, int value, Pair p) {
		i += 1;
		while (i < this.size) {
			Node n = this.nodes[i];
			if (n.getLen()<= value) {
				Node temp = new Node(value, p.getI(), p.getJ(), p.getBool());
				this.nodes[i] = temp;
			}
			i += (i&-i);
		}
	}
	
	// A helper method to instantiate the Array of Nodes so that all of them have the empty value
	public Node[] StartArray(int n) {
		Node[] arr = new Node[n];
		for (int i=0; i<n; i++) {
			arr[i] = new Node();
		}
		return arr;
	}
}
