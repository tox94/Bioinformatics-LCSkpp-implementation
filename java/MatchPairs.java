/** @author Toni Bakarcic */
/** class for calculating all k-sized substring pairs between two input strings*/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class MatchPairs {

	// Private variable that stores the size of the alphabet used in the input file
	private int size;
	// Private variable that stores all the Pairs
	private ArrayList<Pair> allPairs;

	public MatchPairs(int k, String x, String y) {
		this.size = 0;
		// A map for storing all the unique characters and their codes
		HashMap<Character, Integer> map = init(x, y);
		HashMap<Integer, ArrayList<Integer>> table = new HashMap<Integer, ArrayList<Integer>>();
		ArrayList<Pair> pairs = new ArrayList<Pair>();
		ArrayList<Pair> pairsE = new ArrayList<Pair>();
		int mask = (int) (Math.pow(2, this.size*k)-1);

		// Hash value of the first character
		int h = RHash(0, map.get(x.charAt(0)), this.size, k, mask);
		for(int i = 1; i< k; i++) {
			h = RHash(h, map.get(x.charAt(i)), this.size, k, mask);
		}
		if (!table.containsKey(h)) {
			ArrayList<Integer> temp = new ArrayList<Integer>();
			temp.add(0);
			table.put(h, temp);
		}
		// Creating hash values for all the characters in the first string
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
			// Creating hash values for all the characters in the second string
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
		// create the inverse pairs
		int r = pairs.size();
		pairs.forEach((p) -> {
			pairsE.add(new Pair(p.getI() + k, p.getJ() + k, false));
		});
		// add the inverse pairs to the list of all pairs
		pairs.addAll(pairsE);
		Collections.sort(pairs);
		this.size = r;
		this.allPairs = pairs;
	}

	// procedure for finding all unique characters used in the input format and calculating their codes
	public HashMap<Character, Integer> init(String x, String y){
		int i = 0;
		// find all unique characters in the first string
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		for (char c : x.toCharArray()) {
			if (!map.containsKey(c)) {
				map.put(c, i);
				i+=1;
			}
		}
		// find all unique characters in the first string
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

	// rolling hash function
	public int RHash (int h, int y, int b, int k, int mask) {
		// remove the oldest character
		h <<= b;
		// append the new code
		h += y;
		// apply the mask
		h &= mask;
		return h;
	}

	// procedure for returning all the generated Pairs
	public ArrayList<Pair> getPairs(){
		return this.allPairs;
	}

	// procedure for returning the size of the alphabet
	public int getSize() {
		return this.size;
	}
}
