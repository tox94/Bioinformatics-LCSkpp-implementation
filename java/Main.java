import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {
	
	
	public static void main(String[] args) throws IOException {
		
		int cnt = args.length;
		if(cnt != 3) {
			System.out.println("Required 1 file with 2 sequences and k value");
			return;
		}
		
		int k = Integer.parseInt(args[1]);
		//int k = 1;
		BufferedReader reader;
		String x = "";
		String y = "";
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
		System.out.println("Najveæa duljina: " + maxLen);
	}
}
