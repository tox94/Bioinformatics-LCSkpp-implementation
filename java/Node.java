/** @author Toni Bakarcic */
/** a helper class for storing all Pairs and their lengths*/

public class Node {
	
	// variable that stores the length
	private int len;
	// variables that store the starting positions of strings
	private int i;
	private int j;
	// variable is True if the Pair is starting
	private boolean bool;
	
	public Node(int len, int i, int j, boolean bool) {
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
		this.bool = true;
	}
	
	// override method so that the Nodes can be hashed in a more effiecient manner
	@Override
    public int hashCode() {
        return (i<<8) + j;
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
	public boolean getBool() {
		return this.bool;
	}
}
