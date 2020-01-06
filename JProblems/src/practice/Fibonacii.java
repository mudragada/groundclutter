package practice;
import java.io.*;
import java.io.BufferedReader;
import java.io.IOException;

public class Fibonacii {

	public static void main(String[] args) {
		
		int input=0;
		System.out.println("Select a number in range (1-10000)");

		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			input = Integer.parseInt(br.readLine());
		}
		catch (NumberFormatException | IOException e) {
			System.out.println("Invalid Input");
			System.exit(0);
		}
		
		int iCur = 0;
		int iNext = 1;
		
		while (iCur <= input) {
			System.out.println(iCur);
			int addendum = iCur + iNext;
			iCur = iNext;
			iNext = addendum;
		}
	}

}
