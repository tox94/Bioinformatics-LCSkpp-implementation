import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class LCSkpp {
	
	private int maxLen;
	private Pair first;
	private String s1m = "", s2m = "", test1m = "", test2m = "";
	private int iPrev, jPrev;
	
	public LCSkpp(int k, String x, String y) {
		int n = y.length();
		FenwickTree maxColDP = new FenwickTree(n);
		MatchPairs mp = new MatchPairs(k, x, y);
		ArrayList<Pair> events = mp.getPairs();
		HashMap<Pair, Node> dp = new HashMap<Pair, Node>();
		HashMap<Pair, Pair> continueMap = new HashMap<Pair, Pair>();
		ArrayList<Integer> path = new ArrayList<Integer>();
		
		events.forEach((Pair event) -> {
			if (event.getBool() == false) {
				dp.put(event, new Node());
				continueMap.put(new Pair(event.getI() + 1,  event.getJ() + 1, event.getBool()), event);
			}
		});
		
		events.forEach((Pair event) -> {
			if (event.getBool() == false) {
				Node temp = maxColDP.get(event.getI());
				dp.put(event, new Node(temp.getLen() + k, temp.getI(), temp.getJ(), temp.getBool()));
			}else {
				Pair p = new Pair(event.getI() - k, event.getJ() - k, false);
				Pair p2 = continueMap.get(p);
				if(p2 != null) {
					dp.put(p, new Node(dp.get(p2).getLen() + 1, p2));
				}
				maxColDP.update(event.getJ(), dp.get(p).getLen(), p);
			}
		});
		
		this.maxLen = 0;
		first = new Pair(0, 0, false);
		ArrayList<Pair> keys = new ArrayList<Pair>();
		keys.addAll(dp.keySet());
		Collections.sort(keys);
		keys.forEach((Pair child) -> {
			Node temp = dp.get(child);
			if (temp.getLen() >= this.maxLen) {
				this.maxLen = temp.getLen();
				first = child;
			}
		});
		path.add(first.getI());
		path.add(first.getJ());
		Pair child = this.first;
		
		Pair parent = new Pair(0, 0, false);
		while(true) {
			Node temp = dp.get(child);
			parent = new Pair(temp.getI(), temp.getJ(), temp.getBool());
			if (parent.equals(new Pair(-1, -1, false)) || parent.equals(new Pair(0, 0, false)))
				break;
			path.add(parent.getI());
			path.add(parent.getJ());
			child = parent;
		}
		Collections.sort(path, Collections.reverseOrder());
		this.iPrev = -k;
		this.jPrev = -k;
		path.forEach((Integer step) -> {
			int i = step;
			int j = step;
			int cri = 0, chi = 0, crj = 0, chj = 0;
			if (i - iPrev >= k) {
				cri = i - iPrev - k;
			}else {
				chi = k - 1;
			}
			if (j - jPrev >= k) {
				crj = j - jPrev - k;
			}else {
				chj = k - 1;
			}
			this.s1m += generateString("-", cri);
			this.s2m += generateString("-", crj);
			this.test1m += x.substring(i + chi, i + k);
			this.test2m += y.substring(j + chj, j + k);
			this.s1m += x.substring(i + chi, i +k);
			this.s2m += y.substring(j + chj, j +k);
			this.iPrev = i;
			this.jPrev = j;
		});
		
		this.s1m += generateString("-", x.length() - s1m.length());
		this.s2m += generateString("-", y.length() - s2m.length());
		
		System.out.println(s1m.length());
		System.out.println(x);
		System.out.println(s1m);
		System.out.println("\n");
		System.out.println(y);
		System.out.println(s2m);
		System.out.println("\n");
		System.out.println(test1m.length());
		System.out.println(test1m);
		System.out.println(test2m);
		System.out.println("\n");
	}
	
	public String generateString(String s, int n) {
		String str = "";
		for (int i=0; i<n; i++)
			str += s;
		return str;
	}

	public int getLCSkpp () {
		return this.maxLen;
	}

}
