/** @author Toni Bakarcic */
/** a helper class for storing all Pairs*/

import java.util.Comparator;

public class Pair implements Comparable<Object>{
	
	// Startig positions of strings
	private int i;
	private int j;
	// If the Pair is a start, then bool is True
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
	
	// override of the equals method so that the Pairs can be sorted
	@Override
	public boolean equals(Object o) {
		Pair p = (Pair) o;
		return (this.i == p.getI()) && (this.j == p.j) && (this.bool == p.getBool());
	}
	
	// override of the equals method so that the Pairs can be hashed in a more efficient manner
	@Override
    public int hashCode() {
        return (i<<8) + j;
    }

	// override of the equals method so that the Pairs can be compared
	@Override
	public int compareTo(Object comp) {
		return Comparator.comparingInt(Pair::getI).thenComparingInt(Pair::getJ).compare(this, (Pair) comp);
	}

}
