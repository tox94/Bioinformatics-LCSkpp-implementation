import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class MatchPairs {

	private int size;
	private ArrayList<Pair> allPairs;

	public MatchPairs(int k, String x, String y) {
		this.size = 0;
		HashMap<Character, Integer> map = init(x, y);
		HashMap<Integer, ArrayList<Integer>> table = new HashMap<Integer, ArrayList<Integer>>();
		ArrayList<Pair> pairs = new ArrayList<Pair>();
		ArrayList<Pair> pairsE = new ArrayList<Pair>();
		int mask = (int) (Math.pow(2, this.size*k)-1);

		int h = RHash(0, map.get(x.charAt(0)), this.size, k, mask);
		for(int i = 1; i< k; i++) {
			h = RHash(h, map.get(x.charAt(i)), this.size, k, mask);
		}
		if (!table.containsKey(h)) {
			ArrayList<Integer> temp = new ArrayList<Integer>();
			temp.add(0);
			table.put(h, temp);
		}
		for (int i = k; i<x.length(); i++) {
			h = RHash(h, map.get(x.charAt(i)), this.size, k, mask);
			if (!table.containsKey(h)) {
				ArrayList<Integer> temp = new ArrayList<Integer>();
				temp.add(i-k+1);
				table.put(h, temp);
			}else {
				table.get(h).add(i-k+1);
			}
		}

		h = RHash(0, map.get(y.charAt(0)), this.size, k, mask);
		for(int i = 1; i< k; i++) {
			h = RHash(h, map.get(y.charAt(i)), this.size, k, mask);
		}
		if (table.containsKey(h)) {
			ArrayList<Integer> temp = table.get(h);
			for (int i=0; i< temp.size(); i++) {
				pairs.add(new Pair(temp.get(i), 0, true));
			}

		}
		for (int j = k; j<y.length(); j++) {
			h = RHash(h, map.get(y.charAt(j)), this.size, k, mask);
			if (!table.containsKey(h)) {
				continue;
			}
			int val = j -k + 1;
			ArrayList<Integer> temp = table.get(h);
			for (int i=0; i< temp.size(); i++) {
				pairs.add(new Pair(temp.get(i), val, true));
			}
		}

		int r = pairs.size();
		pairs.forEach((p) -> {
			pairsE.add(new Pair(p.getI() + k, p.getJ() + k, false));
		});
		pairs.addAll(pairsE);
		Collections.sort(pairs);
		this.size = r;
		this.allPairs = pairs;
	}

	public HashMap<Character, Integer> init(String x, String y){
		int i = 0;
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		for (char c : x.toCharArray()) {
			if (!map.containsKey(c)) {
				map.put(c, i);
				i+=1;
			}
		}
		for (char c : y.toCharArray()) {
			if (!map.containsKey(c)) {
				map.put(c, i);
				i+=1;
			}
		}
		i -= 1;
		int b = 1;
		while (i != 1) {
			i >>= 1;
			b += 1;
		}
		this.size = b;
		return map;
	}

	public int RHash (int h, int y, int b, int k, int mask) {
		h <<= b;
		h += y;
		h &= mask;
		return h;
	}

	public ArrayList<Pair> getPairs(){
		return this.allPairs;
	}

	public int getSize() {
		return this.size;
	}
}
