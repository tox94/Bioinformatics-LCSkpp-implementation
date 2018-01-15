
public class Node {
	
	private int len;
	private int i;
	private int j;
	
	public Node(int len, int i, int j) {
		this.len = len;
		this.i = i;
		this.j = j;
	}
	
	public Node() {
		this.len = 0;
		this.i = -1;
		this.j = -1;
	}
	
	public int getLen() {
		return this.len;
	}
	public int getI() {
		return this.i;
	}
	public int getJ() {
		return this.j;
	}
}
