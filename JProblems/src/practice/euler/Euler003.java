package practice.euler;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class Euler003 {
	
	public static void main(String[] args) {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter a number in range (1-1000)");
		try {
			int input = Integer.parseInt(br.readLine());
			for (int i=1; i<= Math.sqrt(input); i++) {
				if(input%i == 0) {
					System.out.println(i);
					System.out.println(input/i);
				}
			}
		}
		catch (NumberFormatException | IOException e) {
			System.out.println("Invalid Input");
			System.exit(0);
		}
		
	}


}
