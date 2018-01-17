/** @author Toni Bakarcic */
/** The main class that creates all the needed structures and starts the algorithm*/

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		// Check if all the arguments are provided
		int cnt = args.length;
		if(cnt != 3) {
			System.out.println("Required 1 file with 2 sequences and k value");
			return;
		}

		int k = Integer.parseInt(args[1]);
		System.out.println(k);
		//int k = 1;
		BufferedReader reader;
		String x = "";
		String y = "";
		// read the two strings that will be compared
		try {
			reader = new BufferedReader(new FileReader(args[2]));
			//reader = new BufferedReader(new FileReader("fs.txt"));
			x = reader.readLine();
			y = reader.readLine();
			reader.close();
		} catch (FileNotFoundException e) {
			System.out.println("File not found");
			return;
		}
		LCSkpp l = new LCSkpp(k, x, y);
		int maxLen = l.getLCSkpp();
		System.out.println("Najveca duljina: " + maxLen);
	}
}
