import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class LCSkpp {
	
	private String WORKSPACE_PATH = "";
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
		ArrayList<Pair> path = new ArrayList<Pair>();
		
		for (int i = 0; i < events.size(); i++) {
			Pair event = events.get(i);
			if (event.getBool() == true) {
				Node temp = maxColDP.get(event.getJ());
				continueMap.put(new Pair(event.getI() + 1,  event.getJ() + 1, event.getBool()), event);
				dp.put(event, new Node(temp.getLen() + k, temp.getI(), temp.getJ(), temp.getBool()));
			}else {
				Pair p = new Pair(event.getI() - k, event.getJ() - k, true);
				Object p2 = continueMap.get(p);
				if(p2 != null) {
					dp.put(p, new Node(dp.get((Pair)p2).getLen() + 1, (Pair)p2));
				}
				maxColDP.update(event.getJ(), dp.get(p).getLen(), p);
			}
		}
		
		this.maxLen = 0;
		first = new Pair(0, 0, true);
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
		path.add(first);
		Pair child = this.first;
		
		Pair parent = new Pair(0, 0, true);
		while(true) {
			Node temp = dp.get(child);
			if (temp != null)
				parent = new Pair(temp.getI(), temp.getJ(), temp.getBool());
			if ((parent.getI() == -1 && parent.getJ() == -1 && parent.getBool() == true) 
					|| (parent.getI() == 0 && parent.getJ() == 0 && parent.getBool() == true))
				break;
			path.add(parent);
			child = parent;
		}
		Collections.sort(path);
		this.iPrev = -k;
		this.jPrev = -k;
		path.forEach((Pair step) -> {
			int i = step.getI();
			int j = step.getJ();
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
		
		try {
			File file = new File(WORKSPACE_PATH, "/output.txt");
			
			FileWriter fw = new FileWriter(file);
			fw.write(s1m.length());
			fw.write("\n");
			fw.write(x);
			fw.write(s1m);
			fw.write("\n");
			fw.write(y);
			fw.write(s2m);
			fw.write("\n");
			fw.write(test1m.length());
			fw.write(test1m);
			fw.write(test2m);
			fw.write(String.valueOf(test1m.equals(test2m)));
			fw.write("\n");
			fw.close();
		} catch (IOException e) {
			System.out.println("Output file error.");
		}	
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
