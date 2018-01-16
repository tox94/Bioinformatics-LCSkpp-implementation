
public class FenwickTree {
	
	private Node[] nodes;
	private int size;

	public FenwickTree(int k) {
		this.nodes = StartArray(k + 1);
		this.size = k + 1;
	}
	
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
			i -= (i&-i);
		}
		return n;
	}
	
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
	
	public Node[] StartArray(int n) {
		Node[] arr = new Node[n];
		for (int i=0; i<n; i++) {
			arr[i] = new Node();
		}
		return arr;
	}
}
