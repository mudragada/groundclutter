package practice.euler;

import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 

public class Euler001 {

	public static void main(String[] args) {
		BufferedReader reader =  new BufferedReader(new InputStreamReader(System.in)); 
		
		int input=0, sum=0;
		try {
			System.out.println("Enter a number in the range (1-10000)");
			input = Integer.parseInt(reader.readLine());
		} catch (NumberFormatException | IOException e) {
			System.out.println("Invalid input");
			System.exit(0);
		}
		for (int i=0; i < input; i++) {
			if(i%3==0 | i%5==0) {
				System.out.println(i);
				sum += i;
			}
			else
				continue;
		}
		System.out.println("Sum of the multiples of 3s and 5s is " + Integer.toString((sum)));
	}
}
