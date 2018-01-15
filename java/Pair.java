
public class Pair implements Comparable<Object>{
	
	private int i;
	private int j;
	private Boolean bool;
	
	public Pair(int i, int j, Boolean bool) {
		this.i = i;
		this.j = j;
		this.bool = bool;
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
		int x = ((Pair)comp).getI();
		return this.getI() - x;
	}

}
