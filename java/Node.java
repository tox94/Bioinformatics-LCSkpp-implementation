
public class Node {
	
	private int len;
	private int i;
	private int j;
	private Boolean bool;
	
	public Node(int len, int i, int j, Boolean bool) {
		this.len = len;
		this.i = i;
		this.j = j;
		this.bool = bool;
	}
	
	public Node(int value, Pair p) {
		this.len = value;
		this.i = p.getI();
		this.j = p.getJ();
		this.bool = p.getBool();
	}
	
	public Node() {
		this.len = 0;
		this.i = -1;
		this.j = -1;
		this.bool = false;
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
	public Boolean getBool() {
		return this.bool;
	}
}
