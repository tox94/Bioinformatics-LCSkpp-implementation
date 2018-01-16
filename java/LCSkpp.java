import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class LCSkpp {
	
	private int maxLen;
	private Pair first;
	
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
		int prev = -k;
		String s1m, s2m, test1m, test2m = "";
		path.forEach((Integer step) -> {
			int i = step;
			int j = step;
			int cri, chi, crj, chj = 0;
			if (i - prev >= k) {
				cri = i - prev - k;
			}else {
				chi = k - 1;
			}
			if (j - prev >= k) {
				crj = j - prev - k;
			}else {
				chj = k -1;
			}
		});
	}

	public int getLCSkpp () {
		return this.maxLen;
	}

}
