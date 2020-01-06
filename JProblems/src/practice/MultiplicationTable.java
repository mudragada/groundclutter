package practice;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class MultiplicationTable {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int input=0, times = 1;
		
		try {
			System.out.println("Select a number in range (1-10000)");
			input = Integer.parseInt(br.readLine());
			
			System.out.println("Select number of lines in range (1-50)");
			times = Integer.parseInt(br.readLine());
		}
		catch (NumberFormatException | IOException e) {
			System.out.println("Invalid Input");
			System.exit(0);
		}
		long start = System.currentTimeMillis();

		for (int i=1; i<=times; i++) {
			System.out.println(Integer.toString(input) + " x " + Integer.toString(i) + " = " + Integer.toString(input * i));
		}
		
		long finish = System.currentTimeMillis();
		long timeElapsed = finish - start;
		System.out.println("Time the program took to print - " + timeElapsed + " milliseconds");


	}
}
