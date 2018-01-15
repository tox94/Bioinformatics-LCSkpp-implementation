
public class FenwickTree {
	
	private Node[] nodes;
	private int size;

	public FenwickTree(int k) {
		this.nodes = StartArray(k + 1);
		this.size = k + 1;
	}
	
	public Node get(int i) {
		Node n = null;
		int res = 0;
		i += 1 ;
		while(i >= 0) {
			Node temp = this.nodes[i];
			if (temp.getLen() > res) {
				res = temp.getLen();
				n = temp;
			}
			i = (i & (i + 1)) - 1;
		}
		return n;
	}
	
	public void update(int i, int value) {
		i += 1;
		while (i < this.size) {
			Node n = this.nodes[i];
			if (n.getLen()<= value) {
				Node temp = new Node(value, n.getI(), n.getJ());
				this.nodes[i] = temp;
			}
			i |= i+1;
		}
	}
	
	public Node[] StartArray(int n) {
		Node[] arr = null;
		for (int i=0; i<n; i++) {
			arr[i] = new Node();
		}
		return arr;
	}
}
