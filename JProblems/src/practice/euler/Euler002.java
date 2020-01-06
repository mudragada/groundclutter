package practice.euler;

public class Euler002 {

	static int fib(int n) 
    { 
    if (n <= 1) 
       return n; 
    return fib(n-1) + fib(n-2); 
    } 
	
	public static void main(String[] args) {
		
		int iCur = 1, fibTotal = 0, iFibCur = 0;
		while (iFibCur<=4e6) {
			iFibCur = fib(iCur);
			System.out.println(iFibCur);
			if(iFibCur%2 == 0)
				fibTotal += iFibCur; 
			iCur++;
		}
		System.out.println("Total= " + Integer.toString(fibTotal));
	}

}
