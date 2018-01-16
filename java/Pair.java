import java.util.Comparator;

public class Pair implements Comparable<Object>{
	
	private int i;
	private int j;
	private boolean bool;
	
	public Pair(int i, int j, boolean bool) {
		this.i = i;
		this.j = j;
		this.bool = bool;
	}
	
	public Pair() {
		this.i = -1;
		this.j = -1;
		this.bool = true;
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
	
	@Override
	public boolean equals(Object o) {
		Pair p = (Pair) o;
		return (this.i == p.getI()) && (this.j == p.j) && (this.bool == p.getBool());
	}
	
	@Override
    public int hashCode() {
        return (i<<8) + j;
    }

	@Override
	public int compareTo(Object comp) {
		return Comparator.comparingInt(Pair::getI).thenComparingInt(Pair::getJ).compare(this, (Pair) comp);
	}

}
