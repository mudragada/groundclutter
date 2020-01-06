package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EvenOrOdd {

	public static void main(String[] args) {
		int input=0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			try {
				System.out.println("Select a number in range (1-10000)");
				input = Integer.parseInt(br.readLine());
			}
			catch (NumberFormatException | IOException e) {
				System.out.println("Invalid Input");
				System.exit(0);
			}
		
			String outputMsg = input%2==0? "The Number is even" : "The Number is odd";
		
			System.out.println(outputMsg);
		}
	}

}
