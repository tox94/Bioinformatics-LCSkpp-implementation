import java.util.Comparator;

public class Pair implements Comparable<Object>{
	
	private int i;
	private int j;
	private Boolean bool;
	
	public Pair(int i, int j, Boolean bool) {
		this.i = i;
		this.j = j;
		this.bool = bool;
	}
	
	public Pair() {
		this.i = -1;
		this.j = -1;
		this.bool = false;
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

	@Override
	public int compareTo(Object comp) {
		return Comparator.comparingInt(Pair::getI).thenComparingInt(Pair::getJ).compare(this, (Pair) comp);
	}

}
